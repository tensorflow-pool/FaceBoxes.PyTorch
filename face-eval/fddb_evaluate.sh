./fddb_evaluate -a ../data/FDDB/img_list_ellipseList.txt -d ../eval/maysa_FDDB_dets.txt -f 0 -l ../data/FDDB/img_list.txt -i ../data/FDDB/images/ -r ./detections/fddb/MaysaFaceboxes

python plot_AP_fddb.py
