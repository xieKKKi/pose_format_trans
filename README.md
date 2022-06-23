# pose_format_trans
SLAM轨迹格式转换，在tum格式与位姿矩阵格式之间转换。
其实就是四元数与旋转矩阵之间的转换。
输入文件示例已经给出。
### 用法
```
python mat2quat.py --path=camera_pose_matrix.txt


python quat2mat.py --path=camera_pose.txt
```
