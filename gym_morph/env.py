#!/usr/bin/env python
from gym import Env

# Based on the MuJoCo Ant model
SPECIES = ['longleg',  # morphing - extends first leg joint
           'longfoot',  # morphing - extends second leg joint
           'insect',  # non-morphing - 6 two-joint legs
           'lifter',  # non-morphing - extra lifing joint in hip
           'triple',  # non-morphing - three leg joints
           'ant']  # non-morphing - 4 two-joint legs

TASK = ['run',  # Run as fast as possible in a single direction
        'flagrun',  # Run to a specified 2d location
        'twister']  # Place foot on a specified spot


class MorphEnv(Env):
    def __init__(self, species='ant', task='run'):
        assert species in SPECIES, 'Invalid species'
        self.species = species
        self.task = task
        self.seed = 0  # Used to generate random initial states

    def _reset(self):
        # Use seed to generate random state
        # Use random state to generate:
        #   init pos, init rotation, init joint position, task goal locations
        pass

    def _step(self):
        pass

    def _render(self):
        pass

    def _seed(self, seed=None):
        if seed is not None:
            self.seed = seed
        return [self.seed]
