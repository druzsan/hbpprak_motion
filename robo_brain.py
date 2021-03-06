# -*- coding: utf-8 -*-
"""
This is a minimal brain with 2 neurons connected together.
"""
# pragma: no cover

__author__ = 'Template'

from hbp_nrp_cle.brainsim import simulator as sim
import numpy as np
import logging

logger = logging.getLogger(__name__)

sim.setup(timestep=0.1, min_delay=0.1, max_delay=20.0, threads=1, rng_seeds=[1234])

# Following parameters were taken from the husky braitenberg brain experiment (braitenberg.py)

sensors = sim.Population(3, cellclass=sim.IF_curr_exp())
actors = sim.Population(3, cellclass=sim.IF_curr_exp())

weights = np.random.rand(3, 3) * 5

sim.Projection(sensors, actors, sim.AllToAllConnector(), sim.StaticSynapse(weight=weights))

circuit = sensors + actors
