import numpy as np
import io_layer


def euclid_dis(filepath_in, filepath_out, thresh):
    """Calculates the Euclidean distance for two vektors.

    Args:
        filepath_in (string): The relative file path to the data file.
        filepath_out (string): The relative file path where the output should
        be placed.
        thresh (double integer): The threshhold value that the data should be
            checked against.

    Returns:
    """
#   Read data into np array
    table = io_layer.read_in_np(filepath_in)

#   Remove NaN and remove that column
    np.nan_to_num(table, False, 0)
    table = np.delete(table, 0, 0)

#   Calculate Euclidean Distance per axis
    result_x = np.sqrt(np.sum((table[:, 2]-table[:, 3])**2))
    result_y = np.sqrt(np.sum((table[:, 4]-table[:, 5])**2))
    result_z = np.sqrt(np.sum((table[:, 6]-table[:, 7])**2))
    result = result_x, result_y, result_z

#   Output result as pdf
    io_layer.euclid_dis_plot(filepath_out, result)
    return
