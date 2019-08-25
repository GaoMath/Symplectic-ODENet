from gym.envs.registration import register

register(
    id='MyCartPole-v0',
    entry_point='myenv.cartpole:CartPoleEnv',
)

register(
    id='MyAcrobot-v0',
    entry_point='myenv.acrobot:AcrobotEnv',
)

register(
    id='MyPendulum-v0',
    entry_point='myenv.pendulum:PendulumEnv',
)