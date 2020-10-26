---
layout: post
title: "Beginnings of AI"
date: 2020-10-25 23:05:20 -0400
categories: update
---

# Beginnings of AI

Now that we have created a primitive prototype of our game (we've got basic level generation, a combat protoype, and very basic enemies), it's time to start making some leaps in terms of real AI and procedural generation.

## Enemy AI

Currently, we have an enemy that follows you and shoots you, but not much else. It's purpose is just to test the combat system, so that's all it really needs. But in order for our game to truly be interesting, we need to build a solid AI system.

My main idea for enemy AI involves a blackboard system (UE4 has built-in blackboards, so I might take a look at that!), which can give a kind of hivemind to the AI, which would be perfect for how we want to implement our "Trust" system (think Zombie Pigmen from minecraft). As for individual AI pathfinding, I'll be looking into navmeshes, and for combat I will probably do a more advanced state machine.

## Level Generation

Initially I wasn't too sure how to go about making our level generation algorithm. I was thinking maybe something along the lines of L-Systems, but I stumbled upon a really cool algorithm on YouTube by accident this past week called "Wave Function Collapse". In short, it is based on quantum mechanics, and will take a simple input (such as a 2D texture), and output something of any size that is based on constraints found in the input. However, using this in a 3D context can take a very long time, so I'm planning on using this algorithm to create the layout of each level, and then construct the level based on this (add geometry and objects to build the level structure). I've never used WFC before, so I've been playing with it to see how easily I can get it up and running. My biggest success so far was a really cool WFC sudoku puzzle generator, but that (most likely) won't be a part of our project.

**Writen By: Nate Glick**