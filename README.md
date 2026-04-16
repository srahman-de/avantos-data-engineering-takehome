# Avantos Data Engineering Take Home

## Approach
The solution parses the ASCII art and:

1. Identifies the pupils to determine multiplier value
2. Detects the horizontal span of Angelica's lips
3. Counts polkadots ("O") on the dress
4. Applies the scoring formula:

score =
(# polkadots outside lips range)
+
(# polkadots inside lips range * pupil character count)

## Files
- computePolkadotScore.py → main solution
- ascii_art.txt → ASCII art input

## How to run

python computePolkadotScore.py
