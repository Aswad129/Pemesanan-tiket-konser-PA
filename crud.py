def tambah_data(data_list, new_data):
    """
    Menambahkan data baru ke dalam daftar data.

    Args:
        data_list (list): Daftar data yang ada.
        new_data: Data baru yang akan ditambahkan.

    Returns:
        list: Daftar data yang telah diperbarui dengan data baru.
    """
    data_list.append(new_data)
    return data_list


def view_data():
    """
    Menampilkan data yang ada dalam daftar data.  

    Returns:
        list: Daftar data yang ada.
    """
    # Contoh data awal
    data_list = ["data1", "data2", "data3"]
    return data_list


def update_data(data_list, index, updated_data):
    """
    Memperbarui data pada indeks tertentu dalam daftar data.

    Args:
        data_list (list): Daftar data yang ada.
        index (int): Indeks data yang akan diperbarui.
        updated_data: Data baru yang akan menggantikan data lama.

    Returns:
        list: Daftar data yang telah diperbarui.
    """
    if 0 <= index < len(data_list):
        data_list[index] = updated_data
    return data_list


def hapus_data(data_list, index):
    """
    Menghapus data pada indeks tertentu dalam daftar data.

    Args:
        data_list (list): Daftar data yang ada.
        index (int): Indeks data yang akan dihapus.

    Returns:
        list: Daftar data yang telah diperbarui setelah penghapusan.
    """
    if 0 <= index < len(data_list):
        del data_list[index]
    return data_list