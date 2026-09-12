-- mathbook.lua - the one piece of the design that TeX macros cannot do cleanly.
--
-- \code{...} typesets C exactly as it is written in Chapter 18. \detokenize gets most of the way,
-- but leaves two artifacts that C runs into constantly: it doubles every #, so #include would
-- print as ##include, and it puts a space after every control word, so "\n" would print as
-- "\n ". Both are undone here, and a line break is allowed after a comma, so a long call such as
-- pow(10.0,gain_db/20.0) can break there rather than run into the margin.

local catcode_other = -2

function mathbook_code(s)
  s = s:gsub("#+", "#")
  s = s:gsub("(\\%a+) ", "%1")
  -- \%, \{ and \} are how a literal percent sign or an unbalanced brace has to be written inside
  -- a TeX argument, \# is how a # has to be written in a heading or a caption, and \\ is a
  -- lone backslash.
  s = s:gsub("\\([%%{}#\\])", "%1")
  -- A break is allowed after a comma with no space behind it; a comma followed by a space needs
  -- nothing, because the space is a breakpoint already. Each tex.sprint is read as a line of its
  -- own and TeX skips the spaces a line starts with, so no chunk may begin with one.
  local start = 1
  while true do
    local i = s:find(",[^ ]", start)
    if not i then break end
    tex.sprint(catcode_other, s:sub(start, i))
    -- Discouraged rather than free, so a line breaks at a space when it can.
    tex.sprint("\\penalty100 ")
    start = i + 1
  end
  tex.sprint(catcode_other, s:sub(start))
end
