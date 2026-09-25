# Password Generator

A tiny Python script that creates a random password for you. Made this mostly to mess around with `random` and `math` and actually use them for something instead of just reading about them.

## What it does

Ask it how long you want your password, and it builds one out of three ingredients:

- **Letters** (half the length, randomly upper/lowercased)
- **Numbers** (30% of the length, rounded up so short passwords don't skip this entirely)
- **Special characters** (`@#$%&*`) - whatever length is left over, so everything always adds up correctly

Then it shuffles all of that together so it's not predictably "letters first, then numbers, then symbols."

## How to run it

```bash
python password_generator.py
```

It'll ask for a length, then print your password. That's it.

```
Enter your password length: 12
xR7&K2p9#mQ4
```

## Why I split it up this way

I wanted every password to guarantee a mix of letters, numbers, and symbols instead of leaving that to chance - it's easy to write a generator that *could* technically spit out an all-letters password if you're unlucky. Doing the math up front (half letters, 30% numbers, remainder symbols) means every password has all three, no matter what.

The `math.ceil()` on the numbers is there so short passwords (like length 3 or 4) don't accidentally end up with zero numbers just because the percentage rounded down to nothing.

## Known limitations / stuff I might fix later

- Doesn't check for a minimum password length, so length 1 or 2 will act weird
- No option to exclude certain characters (looking at you, `&` and `%` that some websites hate)
- Could probably use `secrets` instead of `random` if I ever want this to be *actually* secure and not just a fun exercise

## Requirements

Just Python 3. No external packages - `random` and `math` are both built in.