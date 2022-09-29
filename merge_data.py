#!/usr/bin/python3

import argparse
import glob
import re
import os
import csv
from select import select
from shutil import ExecError


def main():
    parser = argparse.ArgumentParser(description = "Merge data from raw files")
    parser.add_argument("-i", "--input", help = "input data folder")
    parser.add_argument("-o", "--output", help = "output csv file")
    args = parser.parse_args()


    if os.path.exists(args.input) == False:
        print("input folder doesn't exist")
        exit(1)

    links_file = ""
    sentences_with_audio_file = ""
    sentences_file = ""

    files = glob.glob(args.input + '/*.csv')

    for file in files:
        if "links.csv" in file:
            links_file = file
        elif "sentences_with_audio.csv" in file:
            sentences_with_audio_file = file
        elif "sentences.csv" in file:
            sentences_file = file

    if links_file == "" or sentences_file == "" or sentences_with_audio_file == "":
        print("invalid input file")
        exit(2)

    audio_map = dict()
    trans_map = dict()
    eng_sentences = dict()
    vie_sentences = dict()

    # mapping sentence and translation into dictionary for querying efficiently with O(1) time complexity
    print("mapping sentence with translation...", end= ' ')
    with open(links_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter='\t')

        for row in csv_reader:
            if not row[0] in trans_map:
                trans_map[row[0]] = set()
            trans_map[row[0]].add(row[1])
    print("done!")

    # mapping sentence and audio url into dictionary for querying efficiently with O(1) time complexity
    print("mapping audio files with sentence...", end=' ')
    with open(sentences_with_audio_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter='\t')

        for row in csv_reader:
            audio_map[row[0]] = row[3]
    print("done!")

    # select all sentences which has lang field is 'eng' or 'vie' for later processing
    print("doing selection english sentences and vietnamese sentences...", end=' ')
    with open(sentences_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter='\t')
        
        for row in csv_reader:
            if row[1] == 'eng':
                eng_sentences[row[0]] = row
            if row[1] == 'vie':
                vie_sentences[row[0]] = row
    print("done!")

    print("combining and writing data...", end=' ')

    with open(args.output, mode='w') as output_csv_file:

        fieldnames = ['id', 'text', 'audio_url', 'translate_id', 'translate_text']
        writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for eng_key in eng_sentences.keys():
            sentence = eng_sentences[eng_key]
            row = dict()

            has_translation = False
            # find transalation in trans_map
            try:
                for trans_key in trans_map[eng_key]:
                    if trans_key in vie_sentences.keys():
                        row['id'] = eng_key
                        row['text'] = eng_sentences[eng_key][2]
                        row['translate_id'] = trans_key
                        row['translate_text'] = vie_sentences[trans_key][2]
                        has_translation = True
            except KeyError as e:
                # sentence doesn't exist in translation map, continue with another sentence
                continue

            try:
                # find audio_url in audio_map
                if eng_key in audio_map.keys():
                    row['audio_url'] = audio_map[eng_key]
            except KeyError as e:
                # sentence doesn't exist in audio map, set it to null
                row['audio_url'] = ''


            # make data consistently
            if not 'audio_url'  in row.keys() or len(row['audio_url']) <= len("http://") :
                row['audio_url'] = 'NULL'

            if has_translation:
                writer.writerow(row)
                
    print("done!")
    print("all things done!")



if __name__ == "__main__":
    main()