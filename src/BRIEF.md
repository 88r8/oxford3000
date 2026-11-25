# Oxford 3000 vocabulary data — brief for each chunk writer

You are writing study data for an Arabic-speaking (Saudi) learner of English. It goes into an offline HTML flashcard app.
Working folder: /private/tmp/claude-501/-Users-salmanfaleh-Desktop-Seu/7c88f780-af25-4189-9478-7f812698e898/scratchpad/ox

## Input
`chunks/cXX.txt` — one word per line, tab-separated: `id <TAB> headword <TAB> parts of speech with CEFR level`.
Headwords may carry a sense hint, e.g. `bank (money)`, `bank (river)`, or a homograph number, e.g. `close1`, `close2` (close1 = shut, close2 = near). Write data for THAT sense only.

## Output
JSON Lines, one object per input line, written in batches of about 40 words to
`out/cXX_01.jsonl`, `out/cXX_02.jsonl`, ... (XX = your chunk number). Use the Write tool (new file per batch). Never rewrite earlier batches unless fixing them.

Object shape (keys exactly these):
{"id": 1, "ipa": "/əˈbændən/", "ar": "يتخلّى عن؛ يهجر", "tr": "أَبَانْدِن", "ex": [{"en": "...", "ar": "..."}, {"en": "...", "ar": "..."}, {"en": "...", "ar": "..."}]}

- **ipa**: British IPA in slashes, main stress marked.
- **ar**: short Arabic meaning(s), the common ones a learner needs, separated by "، ". If the word has more than one part of speech in the list, label them: "(فعل) يعمل، يشتغل · (اسم) عمل، وظيفة". Max ~60 characters per part of speech.
- **tr**: how the English word SOUNDS, written in Arabic letters so a Saudi reader can say it. Conventions: p = پ, v = ڤ, hard g = گ, ch = تش, th (think) = ث, th (this) = ذ, j = ج, short vowels via light تشكيل only where it helps. Example: computer → كَمْبْيُوتَر, village → ڤِلِج, gather → گَاذَر, problem → پْرُوبْلَم.
- **ex**: exactly 3 example sentences (2 is acceptable only for function words like "a", "the", "of"). Each uses the headword (any inflection). Keep them natural, everyday and useful, at roughly the word's CEFR level (A1 words → very simple sentences). If the word has several parts of speech, spread the sentences across them. Write original sentences — do not copy dictionary examples. 6–16 words each. "ar" is a natural Modern Standard Arabic translation.
- Valid JSON only: double quotes, escape inner double quotes, no trailing commas, one object per line.

## Check your work
After every batch run:
`python3 -I validate.py chunks/cXX.txt out/cXX`
Fix any ERR lines. When done the script must print `done N/N | errors 0 | missing 0`.
Then reply with just that final validate line. Do not edit any other files.
