#!/usr/bin/env python

import gym
import gym_morph  # noqa: registers environments
import numpy as np


class LinearAgent:
    def __init__(self, env, loadtxt=None, alpha=.001, sigma=.01):
        self.env = env
        self.alpha = alpha  # Learning Rate
        self.sigma = sigma  # Noise
        obs_size = env.observation_space.shape[0]
        act_size = env.action_space.shape[0]
        if loadtxt is None:
            self.theta = np.random.randn(act_size, obs_size + 1) / obs_size
        else:
            self.theta = np.loadtxt(loadtxt)

    def train(self, epochs=100000):
        for i in range(epochs):
            print('epoch', i)
            self.epoch()
            if i % 10 == 0:
                self.save(i)

    def save(self, i):
        filename = 'evo_{}.txt'.format(i)
        np.savetxt(filename, self.theta)
        print('saved', filename)

    def epoch(self, population=100):
        perturb_shape = (population,) + self.theta.shape
        perturb = np.random.randn(*perturb_shape)
        returns = np.zeros(population)
        for i in range(population):
            returns[i] = self.evaluate(perturb[i])
        print('   best', max(returns))
        self.update(perturb, returns)

    def update(self, perturb, returns):
        norm_returns = (returns - np.mean(returns)) / np.std(returns)
        weighted_perturb = np.einsum('ijk,i', perturb, norm_returns)
        self.theta += self.alpha / (len(returns) * self.sigma) * weighted_perturb

    def evaluate(self, perturb=None):
        obs = env.reset()
        done = False
        reward = 0
        while not done:
            action = self.pi(obs, perturb)
            obs, r, done, _ = self.env.step(action)
            reward += r
        return reward

    def pi(self, obs, perturb=None):
        if perturb is None:
            theta = self.theta
        else:
            theta = self.theta + perturb
        act = np.matmul(theta, np.r_[[1], obs])
        act_space = self.env.action_space
        return np.clip(act, act_space.low, act_space.high)


if __name__ == '__main__':
    env = gym.make('Morph-ant-run-v0')
    la = LinearAgent(env)
    la.train()
