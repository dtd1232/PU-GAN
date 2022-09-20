import argparse
from enum import Flag
import os

def str2bool(x):
    return x.lower() in ('true')

parser = argparse.ArgumentParser()
parser.add_argument('--phase', default='train',help="train/test")
parser.add_argument('--log_dir', default='log') # dir 위치
parser.add_argument('--data_dir', default='data') # dir 위치
parser.add_argument('--augment', type=str2bool, default=True)  # 안바뀌는데.....
parser.add_argument('--restore', action='store_true')
parser.add_argument('--more_up', type=int, default=2)
parser.add_argument('--training_epoch', type=int, default=101)  # training epoch 횟 수
parser.add_argument('--batch_size', type=int, default=28)   # batch_size 크기
parser.add_argument('--use_non_uniform', type=str2bool, default=True)
parser.add_argument('--jitter', type=str2bool, default=False)   # test할 때 사용하지만 정확히 뭘 의미하는지 모르겠음.
parser.add_argument('--jitter_sigma', type=float, default=0.01, help="jitter augmentation") # 마찬가쥐...
parser.add_argument('--jitter_max', type=float, default=0.03, help="jitter augmentation")   # 얘듀...
parser.add_argument('--up_ratio', type=int, default=4)  # 에러
parser.add_argument('--num_point', type=int, default=256)   # 안바뀜
parser.add_argument('--patch_num_point', type=int, default=256)  # 안바뀜
parser.add_argument('--patch_num_ratio', type=int, default=3)   # 시간은 오래 걸리는데 안바뀜
parser.add_argument('--base_lr_d', type=float, default=0.0001)  # 학습률 관련 parameter - 최적화 관련
parser.add_argument('--base_lr_g', type=float, default=0.001) # 학습률 관련 parameter - 최적화 관련
parser.add_argument('--beta', type=float, default=0.9) # 학습률 관련 parameter - 최적화 관련
parser.add_argument('--start_decay_step', type=int, default=50000) # 학습률 관련 parameter
parser.add_argument('--lr_decay_steps', type=int, default=50000) # 학습률 관련 parameter
parser.add_argument('--lr_decay_rate', type=float, default=0.7) # 학습률 관련 parameter
parser.add_argument('--lr_clip', type=float, default=1e-6) # 학습률 관련 parameter
parser.add_argument('--steps_per_print', type=int, default=1) # 출력 횟수
parser.add_argument('--visulize', type=str2bool, default=False) # 출력 여부 확인 파라미터
parser.add_argument('--steps_per_visu', type=int, default=100)  # 출력 횟수 파라미터
parser.add_argument('--epoch_per_save', type=int, default=5)    # 몇번당 모델에 저장하는지
parser.add_argument('--use_repulse', type=str2bool, default=True)   #이건... 
parser.add_argument('--repulsion_w', default=1.0, type=float, help="repulsion_weight")  # 밑 5개는 가중치 관련 파라미터인데 건들면..
parser.add_argument('--fidelity_w', default=100.0, type=float, help="fidelity_weight")
parser.add_argument('--uniform_w', default=10.0, type=float, help="uniform_weight")
parser.add_argument('--gan_w', default=0.5, type=float, help="gan_weight")
parser.add_argument('--gen_update', default=2, type=int, help="gen_update")

FLAGS = parser.parse_args()

