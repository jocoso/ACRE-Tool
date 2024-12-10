

---

# 1937 Planning Coding Sheet (PCS)

A structured plan for developing a modular game system, focusing on abstraction, modularity, and extensibility. This document outlines key components and functionality for a game engine, with a focus on narrative-driven "sessions" and user interaction.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Modules Overview](#modules-overview)
3. [SessionModule Details](#sessionmodule-details)
4. [Naming Conventions](#naming-conventions)
5. [Glossary](#glossary)

---

## Introduction

This project is designed to create a robust game engine that emphasizes narrative flexibility and clear user interaction. It uses abstract base classes (ABCs) and modular architecture for reusability and scalability.

---

## Modules Overview

| **ID**  | **Type** | **Description**                                                                        |
| ------------- | -------------- | -------------------------------------------------------------------------------------------- |
| SessionModule | ABC            | Represents a "chapter" or "scene" in a story, managing progression and transitions.          |
| InputModule   | Module         | Handles player input and command mapping. Ensures proper flow of commands into game logic.   |
| MapModule     | Module         | Implements map handling and layout. Allows adding, removing, or managing rooms in a 2D grid. |

---

## SessionModule Details

| **Field**          | **Type**         | **Description**                                                               |
| ------------------------ | ---------------------- | ----------------------------------------------------------------------------------- |
| `start()`              | Method                 | Starts the session, initializes resources, and calls `on_enter()`.                |
| `stop()`               | Method                 | Stops the session and triggers `on_exit()`.                                       |
| `in_progress()`        | Abstract Method (bool) | Determines if the session is still running. Must be implemented by derived classes. |
| `kill_condition_met()` | Abstract Method (bool) | Checks if the conditions for ending the session have been met.                      |
| `load_resources()`     | Helper Method          | Loads necessary resources for the session.                                          |
| `unload_resources()`   | Helper Method          | Releases resources when the session ends.                                           |
| `on_enter()`           | Hook Method            | Custom logic executed when entering the session.                                    |
| `on_exit()`            | Hook Method            | Custom logic executed when exiting the session.                                     |
| `transition_to_next()` | Helper Method          | Handles transitioning to the next session.                                          |

**Execution Flow:**

1. `on_enter()` is called when the session begins.
2. `start()` initializes execution.
3. `in_progress()` runs repeatedly.
4. If `kill_condition_met()` returns `True`, the session stops, triggering `on_exit()` and transitioning to the next phase.

---

## Naming Conventions

| **Field Name** | **Rules**                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| `player_name`      | Must be between 3 and 50 characters, using only letters, hyphens (`-`), and apostrophes (`'`). |
|                      | Cannot include spaces or special characters outside the allowed set.                               |
|                      | Empty names default to "noor".                                                                     |

**Validation Flow:**

1. Normalize input (trim spaces, convert to lowercase).
2. Check for length restrictions.
3. Validate against character rules.
4. Prompt for confirmation before finalizing.

---

## Glossary

| **Term** | **Meaning**                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------- |
| Soft Error     | An error that doesn't terminate the program but informs the user of a rule violation.                     |
| ABC            | Abstract Base Class. A class designed to be inherited, with at least one method requiring implementation. |
