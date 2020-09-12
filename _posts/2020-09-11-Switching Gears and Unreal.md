---
layout: post
title: "Switching Gears and Unreal"
date: 2020-09-11 23:00:37 -0400
categories: update
---
# What Changed

Overall, we were liking our card game, but we realized that as much as we were making a good game, we were beginning to stray from our idea of having a fast paced game. We discussed our options, and decided to go back to a very old idea we had, without scraping what we already had.

We decided to make a real-time Rogue-like. But instead of tossing our card game ideas, we took the best parts of the card game and turned it into a real-time combat system. It fits the genre pretty well; you construct a deck of attacks that you will quickly cycle through while playing. Cards are randomly spawned around the world, and will act as the main "item collection" mechanic, which is so prevalent in rogue-likes.

We also wanted to make it unique in terms of progression, so we are flipping the "start at the beginning and run to the end" trope on its head. Progression through the game is going to be non-linear, meaning that you will move around to various levels in no particular order. The catch is that balancing would seem to be an issue. We solved this with a mechanic we call "trust", which will affect how enemies react to your presence. Strong enemies will ignore you so long as you don't attack them, or as long as you have a high "trust" value. Fighting enemies in the dungeon will lower your "trust", but it might be necessary to do so in order to beat a run of the game. I don't want to give away too much of the mechanic yet though, so stay tuned for more info.

# Prototyping

Since we now have a clear direction for our game, we decided the best way to continue is to build a prototype of our conbat system. Getting started in UE4 is a little daunting, but we are slowly gaining more familiarity with the engine as we work with it.

<img src="/assets/911/combat.png" width="400" />

We began by getting the UI setup to display our basic attack cards (we only have about 4 that we plan on using to prototype), as well as setting up the actual combat. As of now, we have some basic UI done, as well as a skeleton to build off of for attacking.

#

So far things are going well outside of the occasional hiccup with UE4! Look out for more frequent updates as we get further into development!

**Written By: Nate Glick**