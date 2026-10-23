-- Filtre pandoc : sources markdown de Probabilités I-V -> chapitres LaTeX du poly
-- (même mise en forme que le poly d'Equations différentielles : environnements
-- definition/theoreme/..., exercices en subsubsection*, corrigés regroupés à part).
-- Utilisé par convert.py ; pandoc 2.9.x.

local stringify = pandoc.utils.stringify

local ENVS = {
  definition  = "definition",
  theorem     = "theoreme",
  proposition = "proposition",
  corollary   = "corollaire",
  lemma       = "lemme",
  remark      = "remarque",
  example     = "exemple",
  proof       = "preuve",
}
-- titres qui ne sont que le nom de l'environnement : pas d'argument optionnel
local GENERIC = {
  ["Définition"]=true, ["Définitions"]=true, ["Théorème"]=true, ["Proposition"]=true,
  ["Propositions"]=true, ["Corollaire"]=true, ["Lemme"]=true, ["Remarque"]=true,
  ["Remarques"]=true, ["Exemple"]=true, ["Exemples"]=true, ["Démonstration"]=true,
}
local MARKS = {
  zero  = "\\mathord{\\boldsymbol{\\circ}}",
  one   = "\\mathord{\\bullet}",
  two   = "\\mathord{\\bullet}\\mathord{\\bullet}",
  three = "\\mathord{\\bullet}\\mathord{\\bullet}\\mathord{\\bullet}",
  four  = "\\mathord{\\bullet}\\mathord{\\bullet}\\mathord{\\bullet}\\mathord{\\bullet}",
}

-- classes (avec les coquilles du markdown : answser, prooof, anonyomous)
local function norm_class(c)
  if c:match("^answ") then return "answer" end
  if c:match("^proo") then return "proof" end
  if c:match("^anon") then return "anonymous" end
  return c
end
local function has(classes, name)
  for _, c in ipairs(classes) do if norm_class(c) == name then return true end end
  return false
end

-- même règle que pandoc pour les labels LaTeX
-- préfixe propre au cours (variable d'environnement PROBA_COURSE) : les identifiants
-- des cinq sources se télescopent sinon (ex. defvar en I et en II)
local PREFIX = (os.getenv("PROBA_COURSE") or "") .. (os.getenv("PROBA_COURSE") and "-" or "")
local function lab(id)
  local out = { PREFIX }
  for _, cp in utf8.codes(id) do
    local ch = utf8.char(cp)
    if (ch:match("^[%a%d]$") and cp < 128) or ch:match("^[_%-%+=:;%.]$") then
      out[#out+1] = ch
    else
      out[#out+1] = string.format("ux%x", cp)
    end
  end
  return table.concat(out)
end

local function plain_title(s)
  s = s:gsub("[\\{}$%^_#%%&~]", "")
  return s
end

local function raw(s) return pandoc.RawInline("latex", s) end

local function append_all(dst, src) for _, x in ipairs(src) do dst[#dst+1] = x end end

-- identifiants des corrigés (pour ne mettre un renvoi que s'il y a une solution)
local answer_ids = {}
local known_ids = {}

local function collect_ids(doc)
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      if b.identifier ~= "" then known_ids[b.identifier] = true end
      if has(b.classes, "answer") and b.identifier ~= "" then answer_ids[b.identifier] = true end
    end
  end
end

local function title_marks(h)
  local m = ""
  for _, k in ipairs({"zero","one","two","three","four"}) do
    if has(h.classes, k) then m = " (\\(" .. MARKS[k] .. "\\))" end
  end
  return m
end

local missing_targets = {}

local function build(doc)
  collect_ids(doc)
  local out = {}
  local env = nil          -- environnement ouvert
  local last_is_head = false
  local pending = {}       -- pending[level] = id de l'exercice dont le renvoi "Solution" reste à poser
  local in_sol = false

  local function emit(b, is_head) out[#out+1] = b; last_is_head = is_head or false end
  local function emit_raw(s) emit(pandoc.RawBlock("latex", s)) end

  local function attach_inline(inl)
    local last = out[#out]
    if last and (last.t == "Para" or last.t == "Plain") and not last_is_head then
      local c = last.content
      -- un renvoi après une formule en display ou une figure : nouveau paragraphe
      local lastc = c[#c]
      if lastc and (lastc.t == "Image" or (lastc.t == "Math" and lastc.mathtype == "DisplayMath")) then
        emit(pandoc.Plain({inl}))
      else
        c[#c+1] = inl
      end
    else
      emit(pandoc.Plain({inl}))
    end
  end

  local function flush_pending(level)
    for lv = 6, level, -1 do
      if pending[lv] then
        local id = pending[lv]
        pending[lv] = nil
        attach_inline(raw("\\solref{" .. lab("answer-" .. id) .. "}"))
      end
    end
  end

  local function close_env()
    if not env then return end
    if env == "preuve" then
      attach_inline(raw("\\hfill$\\blacksquare$"))
    end
    emit_raw("\\end{" .. env .. "}")
    env = nil
  end

  -- titre "en ligne" (exercices, questions, corrigés) : \runinhead (défini dans poly.tex) plutôt que
  -- \subsubsection en mode runin, qui fait chevaucher le titre suivant quand un saut de page tombe juste après
  local function runin_head(id, ti, tocinl)
    local pre = { raw("\\runinhead{") }
    append_all(pre, ti)
    pre[#pre+1] = raw("}\\phantomsection")
    if tocinl then
      pre[#pre+1] = raw("\\addcontentsline{toc}{subsubsection}{")
      append_all(pre, tocinl)
      pre[#pre+1] = raw("}")
    end
    if id ~= "" then pre[#pre+1] = raw("\\label{" .. lab(id) .. "}") end
    emit(pandoc.Plain(pre), true)
  end

  local function head_blocks(level, id, titleinl, star, tocname, plain)
    if star or level >= 4 then
      runin_head(id, titleinl, tocname and titleinl or nil)
      return
    end
    local pre = {}
    local cmd = ({"chapter","section","subsection","subsubsection","paragraph","subparagraph"})[level]
    if star then cmd = cmd .. "*" end
    -- cibles des liens : \label (les liens utilisent \hyperref). Un \hypertarget autour du titre ouvre un
    -- paragraphe vide qui fait chevaucher le titre et le texte quand le titre tombe en haut de page.
    pre[#pre+1] = raw("\\" .. cmd .. "{")
    if plain then pre[#pre+1] = raw("\\texorpdfstring{") end
    append_all(pre, titleinl)
    if plain then pre[#pre+1] = raw("}{" .. plain .. "}") end
    local post = "}"
    if id ~= "" then post = post .. (star and "\\phantomsection" or "") .. "\\label{" .. lab(id) .. "}" end
    pre[#pre+1] = raw(post)
    emit(pandoc.Plain(pre), true)
    if tocname then
      local toc = { raw("\\addcontentsline{toc}{" .. tocname .. "}{") }
      append_all(toc, titleinl)
      toc[#toc+1] = raw("}")
      emit(pandoc.Plain(toc), true)
    end
  end

  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      local level = b.level
      local classes = b.classes
      local id = b.identifier
      local title = stringify(b.content)
      close_env()
      flush_pending(level)

      if has(classes, "post") or has(classes, "anonymous") or #b.content == 0 then
        -- séparateur : termine l'environnement précédent, sans sortie
      elseif level == 1 and title == "Solutions" then
        in_sol = true
        emit_raw("%%SOLUTIONS-BEGIN%%")
        emit_raw("\\chapter{Solutions}")
      elseif level == 1 then
        if in_sol then emit_raw("%%SOLUTIONS-END%%"); in_sol = false end
        head_blocks(1, id, b.content, false, nil, nil)
      elseif has(classes, "answer") then
        if level <= 2 then
          head_blocks(level, id, b.content, false, nil, nil)
        else
          head_blocks(3, id, b.content, true, "subsubsection", plain_title(title))
        end
      elseif has(classes, "exercise") or has(classes, "question") then
        if level <= 2 then
          head_blocks(level, id, b.content, false, nil, nil)
          if id ~= "" and answer_ids["answer-" .. id] then pending[level] = id end
        else
          local ti = {}
          local generic = has(classes, "question") and not has(classes, "exercise")
          if not generic then ti[#ti+1] = raw("Exercice -- ") end
          append_all(ti, b.content)
          local marks = title_marks(b)
          if marks ~= "" then ti[#ti+1] = raw(marks) end
          -- la table des matières ne reçoit que le titre
          runin_head(id, ti, b.content)
          if id ~= "" and answer_ids["answer-" .. id] then pending[level] = id end
        end
      else
        local envname = nil
        for _, c in ipairs(classes) do
          local n = ENVS[norm_class(c)]
          if n then envname = n; break end
        end
        if envname and level >= 3 then
          local generic = GENERIC[title] or title == ""
          local opt = generic
          if envname == "preuve" then
            emit_raw("\\begin{preuve}")
          else
            if not generic then
              local toc = { raw("\\addcontentsline{toc}{subsection}{") }
              append_all(toc, b.content)
              toc[#toc+1] = raw("}")
              emit(pandoc.Plain(toc), true)
            end
            local bl = { raw("\\begin{" .. envname .. "}") }
            if not generic then
              bl[#bl+1] = raw("[{")
              append_all(bl, b.content)
              bl[#bl+1] = raw("}]")
            end
            -- l'ancre est dans l'environnement : placée avant, elle ouvrirait un paragraphe vide (ligne blanche)
            if id ~= "" then bl[#bl+1] = raw("\\phantomsection\\label{" .. lab(id) .. "}") end
            emit(pandoc.Plain(bl), true)
          end
          env = envname
        else
          -- titre ordinaire
          head_blocks(math.min(level, 4), id, b.content, false, nil, nil)
        end
      end
    elseif b.t == "RawBlock" and b.format == "html" then
      -- commentaires html : ignorés
    elseif b.t == "RawBlock" and b.text:match("^%s*\\%a*newcommand") then
      -- macros : déplacées dans le préambule du poly
      io.stderr:write("MACRO " .. b.text:gsub("\n", " ") .. "\n")
    elseif b.t == "Para" and #b.content > 0 and (function()
        for _, x in ipairs(b.content) do
          if not ((x.t == "Math" and x.text:match("\\%a*newcommand")) or x.t == "Space" or x.t == "SoftBreak") then return false end
        end
        return true
      end)() then
      for _, x in ipairs(b.content) do if x.t == "Math" then io.stderr:write("MACRO " .. x.text .. "\n") end end
    elseif env and (b.t == "Para" or b.t == "Plain") and (function()
        local n = 0
        for _, x in ipairs(b.content) do
          if x.t == "Image" then n = n + 1
          elseif x.t ~= "Space" and x.t ~= "SoftBreak" then return false end
        end
        return n > 0
      end)() then
      -- figure dans un environnement : pas de flottant (tcolorbox n'en accepte pas), légende avec \captionof
      local res = {}
      for _, x in ipairs(b.content) do
        if x.t == "Image" then
          local cap = x.caption
          x.title = ""
          res[#res+1] = raw("\\begin{center}")
          res[#res+1] = x
          if #cap > 0 then
            res[#res+1] = raw("\\captionof{figure}{")
            append_all(res, cap)
            res[#res+1] = raw("}")
          end
          res[#res+1] = raw("\\end{center}")
        end
      end
      emit(pandoc.Plain(res))
    else
      emit(b)
    end
  end
  close_env()
  flush_pending(1)
  if in_sol then emit_raw("%%SOLUTIONS-END%%") end
  return pandoc.Pandoc(out, doc.meta)
end

-- ---------------------------------------------------------------------------
-- Inlines : liens internes avec renvoi de page, images, espaces insécables

local function Link(l)
  if l.target:sub(1, 1) == "#" then
    local id = l.target:sub(2)
    if not known_ids[id] then io.stderr:write("LIEN SANS CIBLE #" .. id .. "\n") end
    local res = { raw("\\protect\\hyperref[" .. lab(id) .. "]{") }
    append_all(res, l.content)
    local nop = false
    for _, c in ipairs(l.classes) do if c == "no-parenthesis" then nop = true end end
    if nop then
      res[#res+1] = raw(" p.~\\pageref*{" .. lab(id) .. "}}")
    else
      res[#res+1] = raw(" (p.~\\pageref*{" .. lab(id) .. "})}")
    end
    return res
  end
end

local function Image(im)
  local src = im.src
  local ext = src:match("%.(%w+)$")
  if ext == "tex" or ext == "py" or ext == "svg" then src = src .. ".pdf" end
  src = src:gsub("^images/", "")
  im.src = src
  if im.identifier ~= "" then im.identifier = lab(im.identifier) end
  local f = io.open("../images/" .. src, "r")
  if f then
    f:close()
    return im
  end
  io.stderr:write("IMAGE MANQUANTE images/" .. src .. "\n")
  return raw("\\fbox{[figure manquante : " .. src:gsub("[_#%%&]", " ") .. "]}")
end

local function Span(s)
  if s.identifier ~= "" then
    s.identifier = lab(s.identifier)
    return s
  end
end

local function fix_spacing(inlines)
  local out, i, n = {}, 1, #inlines
  while i <= n do
    local x, y = inlines[i], inlines[i+1]
    if x.t == "Space" and y and y.t == "Str" then
      local t = y.text
      if t == ";" or t == "?" or t == "!" then
        out[#out+1] = pandoc.Str("\u{202F}" .. t); i = i + 2
      elseif t == ":" then
        out[#out+1] = pandoc.Str("\u{00A0}:"); i = i + 2
      else
        out[#out+1] = x; i = i + 1
      end
    else
      out[#out+1] = x; i = i + 1
    end
  end
  return out
end

return {
  { Pandoc = build },
  { Link = Link, Image = Image, Span = Span, Inlines = fix_spacing },
}
