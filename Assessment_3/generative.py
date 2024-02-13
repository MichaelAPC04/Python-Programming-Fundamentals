"""
This file is part of Assignment 3 of FIT1045, S1 2023.

It contains methods for generating new images from existing images.

@file generative.py
@author
@date
"""
from __future__ import annotations
from ai import predict_number, read_image

def flatten_image(image: list[list[int]]) -> list[int]:
    """
    Flattens a 2D list into a 1D list.
    
    :param image: 2D list of integers representing an image.
    :return: 1D list of integers representing a flattened image.
    """
    return [pixel for row in image for pixel in row] #scaffold code, but nested lst comp, iterates over every row, then pixel in the rows, added and returned in a 1D lst

def unflatten_image(flat_image: list[int]) -> list[list[int]]:
    """
    Unflattens a 1D list into a 2D list.
        
    :param flat_image: 1D list of integers representing a flattened image.
    :return: 2D list of integers.
    """
    
    new_image = [] #create empty list to unflatten the list into
    flat = int(len(flat_image)**0.5) #calculate sqrt of flat image's len as an int 
    for i in range(0, len(flat_image), flat): #iterate over range, starts at 0 to len of flat_image, flat tells the iterator what to increment by (flat image's sqrt)
        new_image.append(flat_image[i:i+flat]) #create and append row of pixels in unflattened image by slicing the iterator to the iterator+flat, 
    return new_image #return the new unflattened image

def check_adjacent_for_one(flat_image: list[int], flat_pixel: int) -> bool:
    """
    Checks if a pixel has an adjacent pixel with the value of 1.
    
    :param flat_image: 1D list of integers representing a flattened image.
    :param flat_pixel: Integer representing the index of the pixel in question.
    :return: Boolean.
    """
    
    size = int(len(flat_image)**0.5) #redfine our sqrt of flat_image's len as an int

    if  flat_pixel >= size and flat_image[flat_pixel - size] == 1: #above check - first part gets the value of the pixel above (checks if it's equal to 1), 'and', second statement checks if current pixel not in first row
        return True
    
    if flat_pixel < len(flat_image) - size and flat_image[flat_pixel + size] == 1: #below check - first part checks if pixel not in last row, 'and', second statement checks value of pixel below (and if it's equal to 1)
        return True

    if flat_pixel % size != 0 and flat_image[flat_pixel - 1] == 1: #left check - first part 'looks' to left (-1) of the pixel, checks if it's 1 (true), 'and', second statement checks which column the current pixel is in  
        return True

    if flat_pixel % size != size - 1 and flat_image[flat_pixel + 1] == 1: #right check - first part 'looks' to the right (+1) of the pixel, checks if it's 1 (true), 'and', second statement checks where the pixel is, and that it's not in the last column
        return True

    return False

def pixel_flip(lst: list[int], orig_lst: list[int], budget: int, results: list, i: int = 0) -> None:
    """
    Uses recursion to generate all possible combinations of flipped arrays where
    a pixel was a 0 and there was an adjacent pixel with the value of 1.

    :param lst: 1D list of integers representing a flattened image.
    :param orig_lst: 1D list of integers representing the original flattened image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :param results: List of 1D lists of integers representing all possible combinations of flipped arrays, initially empty.
    :param i: Integer representing the index of the pixel in question.
    :return: None.
    """
    
    if lst != orig_lst and lst not in results:
        results.append(lst)

    if i == len(lst): #base case, if the length of the list is 0, append, return nothing
        return None

    if budget > 0 and lst[i] == 0 and check_adjacent_for_one(orig_lst, i):
        altered_list = lst.copy()
        altered_list[i] = 1
        pixel_flip(altered_list, orig_lst, budget -1, results, i+1)
    pixel_flip(lst, orig_lst, budget, results, i+1)

def write_image(orig_image: list[list[int]], new_image: list[list[int]], file_name: str) -> None:
    """
    Writes a newly generated image into a file where the modified pixels are marked as 'X'.
    
    :param orig_image: 2D list of integers representing the original image.
    :param new_image: 2D list of integers representing a newly generated image.
    :param file_name: String representing the name of the file.
    :return: None.
    """
    
    with open(file_name, 'w') as text: #open file, 'w' to write, it's stored as 'text' now in write_image function
        for row in range(len(orig_image)): #begin iteration of rows of original image
            for column in range(len(orig_image)): #begin iteration of columns original image
                if orig_image[row][column] != new_image[row][column]: #if the rows and columns don't match, write 'X' in its place
                    text.write('X')
                else: #else, just continue writing the original values (no need to change)
                    text.write(str(orig_image[row][column]))
            text.write('\n') #write new line, this is in line with the first for loop as after each iteration of a row, a new line is made 

def generate_new_images(image: list[list[int]], budget: int) -> list[list[list[int]]]:
    """
    Generates all possible new images that can be generated within the budget.
    
    :param image: 2D list of integers representing an image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :return: List of 2D lists of integers representing all possible new images.
    """
    #unable to complete due to time constraints


if __name__ == "__main__":
    image = read_image("image.txt")
    new_images = generate_new_images(image, 2)
    print(f"Number of new images generated: {len(new_images)}")
    # Write first image to test generation
    write_image(image, new_images[0], "new_image_1.txt") 

