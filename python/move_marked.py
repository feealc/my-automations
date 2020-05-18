import os
import traceback


def get_all_files(folder, extensions=[]):
    all_files = []

    if not os.path.isdir(folder):
        return all_files
    
    for extension in extensions:
        all_files += [Episode(f) for f in os.listdir(folder) if f.endswith(extension)]

    return all_files


def get_all_dirs(folder):
    print('get_all_dirs()')
    all_dirs = []

    if not os.path.isdir(folder):
        print('get_all_dirs() => not a valid dir')
        return all_dirs
    
    all_dirs = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d)) and not d.startswith('ok ') and not d.startswith('### ')]

    return all_dirs


class Episode():
    def __init__(self, name):
        self.name = name
        self.name_clean = self.__clear_name()
        self.is_finale = False
        self.folder_name = self.__get_folder_name()
    

    def __str__(self):
        return f'nome [{self.name}] name clean [{self.name_clean}]'


    def __clear_name(self):
        name_new = self.name

        for extension in FILE_EXTENSION:
            name_new = name_new.replace(extension, '')
        
        return name_new
    

    def __get_folder_name(self):
        # print(f'get_folder_name()')
        folder_name_tmp = ''
        name_split = self.name_clean.split(' ')

        posicao_final = len(name_split) - 1
        if name_split[posicao_final].lower() == 'finale)':
            self.is_finale = True
            posicao_final -= 2
        
        for i, w in enumerate(name_split):
            if i == posicao_final:
                break
            folder_name_tmp += w + ' '

        folder_name_tmp = folder_name_tmp.rstrip()

        temp_split = name_split[posicao_final].split('x')

        folder_name_tmp += f' - {temp_split[0]} Temporada'

        return folder_name_tmp
    

    def move_episode(self):
        # print('move_episode()')
        destination_dir = os.path.join(FOLDER_MARKED, self.folder_name)

        if os.path.isdir(destination_dir):
            file_orig = os.path.join(FOLDER_MARKED, self.name)
            file_dest = os.path.join(FOLDER_MARKED, self.folder_name, self.name)

            try:
                print(f'Movendo [{file_orig}] para [{file_dest}]')
                os.rename(file_orig, file_dest)
            except:
                print('Erro movendo arquivo')
                print(traceback.format_exc())
                exit(0)

            if self.is_finale:
                dir_orig = os.path.join(FOLDER_MARKED, self.folder_name)
                dir_dest = os.path.join(FOLDER_MARKED, 'ok ' + self.folder_name)

                try:
                    print(f'Renomeando diretório [{dir_orig}] para [{dir_dest}]')
                    os.rename(dir_orig, dir_dest)
                except:
                    print('Erro renomeando diretório')
                    print(traceback.format_exc())
                    exit(0)
        else:
            print(f'Diretório não encontrado para [{self.name}]')


if __name__ == "__main__":
    FOLDER_MARKED = 'D:\Series2\MARCADOS'
    FILE_EXTENSION = ['.mp4', '.rmvb']
    # FILE_EXTENSION = ['.mp4', '.rmvb', '.txt']
    # FILE_EXTENSION = ['.txt']

    if not os.path.isdir(FOLDER_MARKED):
        print(f'O diretório {FOLDER_MARKED} não é valido')
        exit(0)

    all_files = get_all_files(FOLDER_MARKED, FILE_EXTENSION)
    for f in all_files:
        # print()
        # print(f)
        f.move_episode()

    # all_dirs = get_all_dirs(FOLDER_MARKED)
    # for d in all_dirs:
    #     print(d)

    print()

