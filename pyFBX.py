from FbxCommon import *
import Modifiers
import argparse
import os

def process_fbx_file(input_path, output_path):
    if os.path.splitext(input_path)[1].lower() != '.fbx':
        print('<PyFBX> : Found wrong file format : ' + input_path)
        return

    sdk_manager, scene = InitializeSdkObjects()
    result = LoadScene(sdk_manager, scene, input_path)
    if result:
        # DisplayHierarchy.display_hierarchy(scene)
        Modifiers.modify_animation(scene)
        SaveScene(sdk_manager, scene, output_path)

def check_output_folder(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Modify FBX file(s)')
    parser.add_argument('-if', '--inputfile', help='input file path. For only one file')
    parser.add_argument('-id', '--inputdir', help='input directory. For multi-files')
    parser.add_argument('-of', '--outputfile', help='output file path. When -if is used, this must be used')
    parser.add_argument('-od', '--outputdir', help='output directory. When -id is used, this must be used')
    args = parser.parse_args()
    if args.inputfile and args.outputfile:
        process_fbx_file(args.inputfile, args.outputfile)
    elif args.inputdir and args.outputdir:
        check_output_folder(args.outputdir)
        for root, folders, files in os.walk(args.inputdir):
            for current_file in files:
                process_fbx_file(os.path.join(root, current_file), os.path.join(args.outputdir, current_file))
    else:
        parser.print_usage()
        parser.print_help()


