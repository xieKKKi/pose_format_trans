# -*- coding: UTF-8 -*-
import argparse
from scipy.spatial.transform import Rotation as RR
import numpy as np


def main(input_path_traj):
    print("**********************************")
    print("processing...")
    lidar_path_name = input_path_traj.split('/')
    file_name = lidar_path_name[-1].split('.')

    with open(input_path_traj, 'r') as f, open(file_name[0] + '_matrix.txt', 'w+') as out_file:
        for line in f.readlines():
            tmp_txt = str.split(line.strip())         
            time0 = float(tmp_txt[0])
            r = RR.from_quat([float(tmp_txt[4]), float(tmp_txt[5]), float(tmp_txt[6]), float(tmp_txt[7])]).as_matrix()
            t = np.matrix([float(tmp_txt[1]), float(tmp_txt[2]), float(tmp_txt[3])])
            T_ = np.hstack([r, t.transpose()]) # 水平拼接
            T = np.vstack([T_, np.array([0, 0, 0, 1])]) # 竖直拼接

            write_txt = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16}\n".format(time0, 
                T[0, 0], T[0, 1], T[0, 2], T[0, 3],
                T[1, 0], T[1, 1], T[1, 2], T[1, 3],
                T[2, 0], T[2, 1], T[2, 2], T[2, 3],
                T[3, 0], T[3, 1], T[3, 2], T[3, 3])
            out_file.writelines(write_txt)
            
    print('\ndone.')
    print("**********************************")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=False, default='camera_pose.txt')
    args = parser.parse_args()
    main(args.path)

