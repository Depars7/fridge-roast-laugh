# Fridge Roast: One Line, Biggest Laugh — design notes

Bounty: Fridge Roast: One Line, Biggest Laugh
(u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb, $5, 3 places).
Gate: `/output/entry.txt`, UTF-8, 1–200 characters, not only whitespace.
Judge (pairwise, blind, criteria in order): (1) a roast of a smart fridge
itself — its app, its firmware, its ice maker; (2) the punchline lands, a
turn or surprise on the first read; (3) specific to smart fridges, not a
generic gadget gag; (4) tight wording, every word earns its place;
(5) fresh angle — avoids the obvious cracks about the fridge ordering
groceries or watching you. A line that explains its own joke has lost.

## Candidates (12, all original, written for this entry)

1. **My smart fridge updated its firmware overnight and forgot how to be cold.** (73) — PICK
2. I asked my smart fridge for ice. It opened the app store. (57)
3. The ice maker in my smart fridge has one job and a union rep. (61)
4. My smart fridge sent me a notification that my milk expired. It cc'd my mother. (79)
5. I paid $3,000 for a fridge that beeps when the door is open. My old one did that for free and never asked for Wi-Fi. (116)
6. My smart fridge's touchscreen froze, so I had to reboot my fridge. My fridge. Reboot. (85)
7. My smart fridge texts me at 3 a.m. that the door is open. I know. I'm standing in front of it. (94)
8. My fridge's ice maker has been "coming soon" since 2021 — the only thing in my kitchen on a roadmap. (100)
9. My smart fridge updated itself and now the ice maker only speaks in error codes. (80)
10. My fridge knows the milk expired before I do, and it tells me like a disappointed landlord. (91)
11. My smart fridge's idea of smart is charging me a subscription to stop judging my midnight snacks. (97)
12. My smart fridge ran out of storage, so it deleted the cold. (59)

## Scoring per judge criterion (1–5)

| # | On-subject | Punchline | Specific | Tight | Fresh | Total |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 5 | 4 | 24 |
| 2 | 4 | 4 | 4 | 5 | 4 | 21 |
| 3 | 5 | 4 | 5 | 5 | 3 | 22 |
| 4 | 4 | 4 | 4 | 4 | 3 | 19 |
| 5 | 4 | 3 | 4 | 3 | 3 | 17 |
| 6 | 5 | 4 | 5 | 4 | 4 | 22 |
| 7 | 4 | 3 | 3 | 3 | 3 | 16 |
| 8 | 5 | 3 | 5 | 4 | 4 | 21 |
| 9 | 5 | 3 | 5 | 4 | 3 | 20 |
| 10 | 4 | 3 | 4 | 4 | 2 | 17 |
| 11 | 4 | 3 | 4 | 3 | 3 | 17 |
| 12 | 4 | 4 | 4 | 5 | 3 | 20 |

## Why #1 wins

- **On-subject (criterion 1):** firmware is named in the judge brief
  itself, and the roast is aimed squarely at the fridge.
- **Punchline (criterion 2):** the turn is the last five words —
  a fridge forgetting how to be cold is a fridge failing its one job.
  The laugh lands on the first read, no explanation needed.
- **Specific (criterion 3):** only a fridge's job is being cold; the
  gag cannot move to a toaster, a TV or a phone.
- **Tight (criterion 4):** 73 characters, one sentence, no setup the
  punchline does not need.
- **Fresh (criterion 5):** no grocery ordering, no camera watching,
  no milk-shaming — the angle is a firmware update breaking the
  appliance's core purpose.

## Why the others lost

- #2: snappy, but "opened the app store" could happen on any smart
  gadget — weaker on specificity; the ice is the only fridge part.
- #3: funny, but "one job" is a known meme format, and the union-rep
  turn is a shrug rather than a surprise.
- #4: the cc'd-my-mother twist is charming, but milk-expiry nagging is
  the lane every entrant will write in.
- #5: a real observation, but two sentences and 116 characters — the
  punchline arrives late and the Wi-Fi jab is generic.
- #6: "reboot my fridge" is a good absurdity, but the repetition
  explains the joke instead of landing it.
- #7: two beats, and a door-open alert is the fridge's most obvious
  feature — the turn is mild.
- #8: "on a roadmap" is a nice collision, but "coming soon" setups
  are familiar and the punchline is soft.
- #9: error codes are a decent turn, but the line reports the joke
  rather than staging it.
- #10: "disappointed landlord" is vivid, yet milk-expiry nagging is
  crowded and the line leans on watching-you territory.
- #11: subscription + midnight-snack judging stacks two ideas; neither
  gets room to land.
- #12: short and punchy, but "deleted the cold" is a weaker turn than
  "forgot how to be cold" — deletion is a storage gag, forgetting is a
  fridge failing at being a fridge.

## Program

`main.py` (stdlib only, no network, no randomness) validates the line
against the gate, writes it to `/output/entry.txt` with no trailing
newline, mode 0644, then reads the bytes back and verifies they match
exactly. Two runs are byte-identical by construction.
