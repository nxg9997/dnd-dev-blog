---
layout: post
title: "Procedural Generation & New Assets"
date: 2021-02-05 20:02:34 -0400
categories: update
---

# Improvements to Procedural Generation

Last time I made a post about procedural generation was when I had finished the initial WFC algorithm. We've made some big progress since then, and the algorithm is fully implemented into the game now!

After lots of trial and error, we found a handful of source patterns for WFC that created excellent layouts for our levels. For a while, we were using some placeholder models for out generation (since we just needed to see if it worked or not), and we finally settled on some models that we thought would be a good fit for the environment. Enemies and the player are still placeholders while we search for either an artist, or some other good models.

Now that we were generating levels with nice environment art, we ran into a new problem: sometimes the level would generate with unconnected areas. This was an issue, because it could mean that some areas were inaccessable, and this could lead to some items being uncollectable, or even worse, the trigger for the next level could be locked inside one of these areas, effectively soft-locking the game. To fix this, I had to figure out a way to modify the output of the WFC algorithm to find and connect isolated regions. The algorithm I built to this recursively searched each level for each of these regions, known in the code as "hulls", and then it does a simple pathfinding algorithm between each of the hulls to create paths where walls used to be.

Here is the generation before I fixed the separate regions:

<img src="/assets/2521/hulls1.png" width="400" />

...And here is the generation after the fix:

<img src="/assets/2521/hulls2.png" width="400" />

In addition, I added some extra visuals, such as mushrooms and rocks, to the generation algorithm to make the level feel a little bit more alive. And of course, enemies spawn in the cave as well (based on the WFC output).

# Upcoming Playtest

We have an upcoming playtest with a class of undergraduate students as our testers on Tuesday. Our plan for the playtest is to learn about our core combat system, and as such we have been working to make sure everything is ready to be put in front of our testers. The Davids have been working hard on making sure all of our attacks and basic UI work well, and I've been making sure the level generation is good enough to allow the players to play inside. One of our goals was to be able to infinitely generate levels, and I was able to make it so that when a player reaches the next level trigger (currently represented by a hole in the ground), the game will generate a new level and plop the player in. Since we aren't testing enemy AI yet, we will be filling the levels with some basic enemies that the player can attack.

Hopefully following the playtest we will have some valuable feedback which we can use to refine our combat system, since this will be the main draw of the game (as it is in other action rogue-likes, such as *Hades*).

Also, having a playtest means that we will have a alpha build of our game, so we can easily distribute it to others who may want to playtest our game as well!

That's all I have for an update for now, but look out for many more updates in the coming weeks as we get more and more into development!

**Written By: Nate Glick**