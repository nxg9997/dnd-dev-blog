---
layout: post
title: "Wave Function Collapse"
date: 2020-11-16 16:19:05 -0400
categories: update
---

# Wave Function Collapse

It's been done! Our solution for procedural generation has been completed (or at least the base algorithm has).

<img src="/assets/1116/wfc.gif" height="400" width="711" />

**Wave Function Collapse** (WFC) is an algorithm inspired by quantum physics, where a wave function is collapsed based on an initial condition. To put it simply, the "wave function" starts as a superposition of all possible solutions (this means that all possible states exist at the same time). We then "observe" a target cell, which means we "collapse" that cell into a single state out of it's possible states. We then "propogate" this change to the rest of the wave function (think "dropping a stone in a puddle"; you see the ripples caused by the stone being dropped), and now every other cell in the wave function now only contains states that are possible based on the initial observation. We repeat this process until the entire wave function has either collapsed, or there is a "contradition" (meaning a cell has no possible states to choose from).

In the end, we are left with a single possible solution for our wave function. In our case, this means we have generated things like a unique level layout, unique rooms, etc. We can specify a pattern that the wave function algorithm can draw from to generate rules for cell states, so we can use the same algorithm for many different uses, depending on what we want to generate with it - we just change the input! Even changing the input by a single cell can drastically change the output, so we get very interesting and unique output on each run!

## Next Steps

Now that the algorithm is working, it needs to be implemented into our project. There are some performance issues, so making very large outputs is not a good idea. However, small outputs should be good for our purposes, and we can run the algorithm in parallel to generate everything much faster. Of course, our project isn't using 2D textures, so instead of drawing squares onto the screen, we will use the output to place tiles in the scene (aka level components or whatever you'd like to call them).

Once this has been ported into the game project, I can start to work on better enemy AI!

**Written By: Nate Glick**