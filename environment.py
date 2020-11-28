from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import obj_actions

from abc import ABC

import numpy as np

from tf_agents.environments import py_environment
from tf_agents.specs import array_spec

from tf_agents.trajectories import time_step as ts


class VolumeFitterEnv(py_environment.PyEnvironment, ABC):

    def __init__(self):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=3, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(1,), dtype=np.int32, minimum=0, name='observation')
        self._state = 0
        self._episode_ended = False
        self.objects = obj_actions.bodies
        self.done = self.objects.pop()

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._state = 0
        self._episode_ended = False
        return ts.restart(np.array([self._state], dtype=np.int32))

    def _step(self, action):

        if self._episode_ended:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self.reset()

        # Stop arranging
        if action == 0:
            self._episode_ended = True
        # Arrange one object
        elif action == 1:
            body = obj_actions.bodies.pop()
            for _ in range(6):
                obj_actions.arrange_cubes(done, body)
                get_outter_box
            self._state += new_card
        # Save changes
        elif action == 2:

        else:
            raise ValueError('`action` should be 0, 1 or 2.')

        if self._episode_ended or self._state >= 21:
            reward = self._state - 21 if self._state <= 21 else -21
            return ts.termination(np.array([self._state], dtype=np.int32), reward)
        else:
            return ts.transition(
                np.array([self._state], dtype=np.int32), reward=0.0, discount=1.0)
