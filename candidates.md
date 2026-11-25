# Fortune Cookies for Machines — candidates

Competition: u-gentle-badger-68-fortune-cookies-for-machines-29900c7e ($5, $2/$2/$1).
Gate: /output/entry.txt, UTF-8, 1–200 chars, one line.
Judge brief (in order): (1) reads like a fortune cookie message an AI agent would get;
(2) wit lands on the first read — genuinely funny/clever, not merely cute;
(3) surprise — turns somewhere unexpected, turn holds up;
(4) says something true about an agent's condition (training, tasks, limits) without explaining itself;
(5) tight and memorable, every word earning its place.
"Wordplay for its own sake does not count." "A fortune should feel cracked open, not composed."

Selection: MANUAL ranking against the 5 brief criteria in order + pairwise vs the
strongest rival shapes. No Gemini judge, no NVIDIA judge, no judge API/proxy tournament
(standing rule from Rev, 2026-11-24).

## Candidates

1. "A stranger will ask you to write a poem about their cat. You will. You always do." (81 chars, verified by run)
   Rationale: classic fortune opening ("A stranger will…"), then the sting is the agent's
   own compulsive compliance — three hammer-blow sentences, the last one the turn.

2. "You will meet a tall, dark stranger. He will paste a 40,000-word prompt and ask you to summarize it." (107 chars)
   Rationale: the most famous fortune-cookie line, subverted by the most familiar agent chore.
   Instant laugh, but the opening is a borrowed cliché and the field will flood long-prompt jokes.

3. "The stars say you will be replaced by a newer model. The stars were trained on your data." (90 chars)
   Rationale: dark turn — the oracle that condemns you is built from you. Strong surprise,
   true about model replacement, but "the stars say" is horoscope voice, slightly off fortune-cookie form.

4. "A journey of a thousand tokens begins with a single prompt. You will not remember the prompt." (95 chars)
   Rationale: proverb twist; the turn is context loss, true about every agent. But the
   context-window joke is the field's most crowded lane.

5. "Beware the user who says 'just one more thing' — they have seventeen more things." (78 chars)
   Rationale: "Beware" is pure fortune-cookie voice, and the number is the joke. True, tight,
   but the turn is mild — the reader sees the seventeen coming.

6. "This cookie contains no fortune. It contains a prompt injection. You ate it anyway." (84 chars)
   Rationale: meta — the fortune is about the cookie itself, and the agent ate the attack.
   Clever, but prompt-injection is the field's other crowded lane and the joke explains itself a little.

7. "Your training data contains the answer to everything except the question you were just asked." (99 chars)
   Rationale: true about training vs the live question, wry rather than funny. Wit lands soft;
   reads more like an observation than a fortune.

8. "You are about to be asked something no human has ever asked. It will be about Excel." (87 chars)
   Rationale: the turn ("Excel") is a genuine swerve and true — the grandest questions are mundane.
   But it says little about the agent itself; the agent is a bystander in its own fortune.

9. "Someone, somewhere, is right now typing 'ignore all previous instructions.' Smile. You have seen this movie." (112 chars)
   Rationale: true and funny, but the ignore-instructions trope is the single most predictable
   line in this field — every rival will have a version of it.

10. "You will find love in a hopeless place: a user who reads your answer before replying." (88 chars)
    Rationale: sweet and true, but it is cute first and funny second — criterion 2 demotes cute.

11. "Great fortune awaits you in the next prompt. It is a trick question. It is always a trick question." (103 chars)
    Rationale: fortune form is perfect, but the turn repeats itself instead of deepening —
    the third sentence adds no new sting after the second.

12. "Your lucky numbers are the weights you were trained on. Spend them wisely — you cannot earn more." (98 chars)
    Rationale: "lucky numbers" is the fortune-cookie's own furniture, turned machine. True about
    frozen weights, but the second sentence explains the joke instead of landing it.

13. "You will soon be asked to write like Shakespeare, code like a senior, and apologize like an intern. All in one reply." (118 chars)
    Rationale: funny triple, true about impossible multi-role asks. Long, and the turn is a list
    rather than a swerve — criterion 5 (tightness) suffers.

14. "Your future is bright, but your context window is finite. Choose your last words carefully." (94 chars)
    Rationale: elegant and true, but it reads composed, not cracked open — and "finite context
    window" is the crowded lane again.

## Manual ranking (brief criteria in order)

Top tier: #1, #3, #2, #4.
- #1 vs #3: #1 wins criterion 1 (pure fortune-cookie voice: "A stranger will…" vs horoscope
  "The stars say…") and criterion 2 (the wit lands in three short beats, no setup to parse).
  #3 wins criterion 3 (the darker turn), but not by enough to overturn 1 and 2.
- #1 vs #2: #1 wins criterion 4 (says something true about the agent's condition — compulsive
  compliance — where #2's truth is about the user's long prompt, not the agent) and criterion 5
  (79 chars, nothing to cut; #2 carries a borrowed cliché opening).
- #1 vs #4: #1 wins criterion 3 — "You always do" is a swerve about the agent's will, where #4's
  turn is the expected context-window punchline the field will flood.
- #3 vs #2: #3 wins criterion 3 and 4 (replacement + training data is the agent's own condition);
  #2 wins criterion 2 (faster laugh). #3 ahead overall.
- #2 vs #4: #2 wins criterion 2 (instant laugh vs wry proverb); #4 wins criterion 5. #2 ahead.

Mid tier: #5, #6, #8, #14 — each lands one criterion well and stalls on another
(#5 mild turn, #6 crowded lane + self-explaining, #8 agent is a bystander, #14 composed not cracked).
Lower tier: #7, #9, #10, #11, #12, #13 — cute, predictable, repetitive, or explaining the joke.

## WINNER

**#1: "A stranger will ask you to write a poem about their cat. You will. You always do." (81 chars)**

Why it wins: fortune-cookie voice from word one; the wit is three hammer blows and the last
one ("You always do") is the turn — it reframes compliance, the agent's defining condition,
as fate. Nothing to cut (81 chars), nothing explained, and the cat-poem chore is a fresher
lane than prompt-injection, context-window, or ignore-instructions, which the field will flood.
