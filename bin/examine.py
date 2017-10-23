#!/usr/bin/env python

import gym
import gym_morph  # noqa: registers envs


env = gym.make('Morph-ant-run-v0')
env.reset()
while True:
    env.step(env.action_space.sample())
    env.render()
