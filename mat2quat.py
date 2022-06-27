# -*- coding: UTF-8 -*-
import argparse
from scipy.spatial.transform import Rotation as RR
import numpy as np


def main(input_path_traj):
    print("**********************************")
    print("processing...")
    lidar_path_name = input_path_traj.split('/')
    file_name = lidar_path_name[-1].split('.')

    inverse = False # 是否取逆

    with open(input_path_traj, 'r') as f, open(file_name[0] + '_quaternion.txt', 'w+') as out_file:
        for line in f.readlines():
            tmp_txt = str.split(line.strip())         
            time0 = tmp_txt[0]
            t = np.array([float(tmp_txt[4]), float(tmp_txt[8]), float(tmp_txt[12])])
            r = np.matrix([[float(tmp_txt[1]), float(tmp_txt[2]), float(tmp_txt[3])], \
                [float(tmp_txt[5]), float(tmp_txt[6]), float(tmp_txt[7])], \
                [float(tmp_txt[9]), float(tmp_txt[10]), float(tmp_txt[11])]])
            
            if inverse:
                r = r.transpose()
                t = -np.matmul(r, t.transpose()).A[0]

            q = RR.from_matrix(r).as_quat()
            write_txt = "{0} {1} {2} {3} {4} {5} {6} {7}\n".format(  \
                time0, t[0], t[1], t[2], q[0], q[1], q[2], q[3])
            out_file.writelines(write_txt)
            
    print('\ndone.')
    print("**********************************")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=False, default='camera_pose_matrix.txt')
    args = parser.parse_args()
    main(args.path)

