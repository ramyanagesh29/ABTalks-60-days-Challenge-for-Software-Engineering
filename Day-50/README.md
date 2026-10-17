# Day 50 — The Superhero Academy Simulator

## Overview
This Python project models heroes with energy levels, powers, and specialized attacks.
It demonstrates core Object-Oriented Programming (OOP) principles.

## Design
- `Hero`: base class containing shared state (`name`, `energy`, `power`) and behavior (`attack`, `take_damage`, `is_active`).
- `FireHero`: inherits from `Hero` and overrides `attack` with a Flame Burst.
- `TechHero`: inherits from `Hero` and overrides `attack` with a Tech Blast.
- `battle()`: alternates attacks until a hero has no energy left.

## OOP concepts
1. **Encapsulation:** each hero stores its own state in an object.
2. **Inheritance:** specialized hero classes reuse the base `Hero` implementation.
3. **Polymorphism:** `battle()` calls `attack()` without needing to know the exact hero type; Python runs the overridden method.
4. **Method overriding:** subclasses provide their own `attack()` behavior.

## Design choices
- Energy is clamped at zero to avoid negative energy.
- The battle loop checks whether both heroes remain active.
- Attack costs differ by hero type, making subclasses meaningfully different.
- To scale the simulator, more hero types can be added by subclassing `Hero` or by later introducing configurable abilities.

## Complexity
A battle runs for a number of turns proportional to total energy divided by typical attack cost. Each turn performs constant-time work, so runtime is **O(T)** for T turns.

## Run
`python day50_superhero_academy.py`
