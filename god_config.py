from easydict import EasyDict as edict

config = edict()


"data and check point directories"
config.raw_image_dir = ''
config.data_tfrecord_dir = './train/whole_dataset.tf'
config.num_of_data = 186961


"optimization"
config.batch_size = 64
config.lr_init = 2e-4
config.beta1 = 0.5
config.beta2 = 0.9

"loss"
config.loss_type = 'sigmoid'
config.recons_loss_w = 40.0
config.e_adverse_loss_w = 8.0
config.g_gen_loss_w = 4.0

config.n_epoch = 100
config.lr_decay = 0.99

"generator type"
config.generator_type = 'dcgan' # or 'dcgan'

config.use_augmentation = True
"summaries"
config.summary_dir = './summary'

config.save_every = 1
config.num_of_update_for_e_g = 2
config.hidden_dim = 128
config.num_of_resblk = 4
