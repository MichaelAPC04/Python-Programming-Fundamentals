from __future__ import annotations
import unittest
#from generative import flatten_image, unflatten_image, check_adjacent_for_one, pixel_flip, write_image, generate_new_images ##testing code with task 3 and 5
from generative import flatten_image, unflatten_image, check_adjacent_for_one, pixel_flip, write_image ##testing code without task 3 and 5
from ai import read_image

###!!!PLEASE NOTE: above I have commented-out the original import for all the tasks, as I did not complete task 5, thus it is omitted from the import to allow all tests to run without an import failure### 

class TestGenerative(unittest.TestCase):
    """Unit tests for the module generative.py"""

    def test_flatten_image(self) -> None:
        """
        Verify output of flatten_image for at least three different sizes of images.
        """

        test_actual_output = [
            [0,0,0],
            [1,1,1],
            [0,1,1]
        ] #2D 3x3 image, unflattened, which will be tested and flattened by the function

        test_expected_output = [0,0,0,1,1,1,0,1,1] #expected answer if flattened correctly (hardcoded)

        self.assertEqual(test_expected_output, flatten_image (test_actual_output)) #test unflattened image in function flatten_image against hardcoded flattened image, assert they're equal, if not, test fails, thus function was coded wrong

        test_actual_output = [
            [1,0,1,1],
            [1,1,1,1],
            [0,0,0,0],
            [0,1,0,1]
        ] #checking a larger size, 4x4 image

        test_expected_output = [1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1]

        self.assertEqual(test_expected_output, flatten_image (test_actual_output)) #same methodology, see the first assertion comment

        test_actual_output = [
            [1,0,1,1,1,0,0,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0,0],
            [1,0,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0],
            [0,0,0,1,1,1,0,0],
            [0,1,0,1,0,1,0,1]
        ] #now we're checking an even larger size, 8x8 image
        
        test_expected_output = [1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1]

        self.assertEqual(test_expected_output, flatten_image (test_actual_output)) #same methodology, see the first assertion comment

    def test_unflatten_image(self) -> None:
        """
        Verify output of unflatten_image for at least three different sizes of flattened images.
        """

        test_actual_output = [1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1] #4x4 flattened image to be checked, will be tested and unflatten by the function 

        test_expected_output = [
            [1,1,0,0],
            [1,0,1,1],
            [0,1,0,1],
            [1,1,1,1]
        ] #expected answer if unflattened correctly (hardcoded)

        self.assertEqual(test_expected_output, unflatten_image (test_actual_output)) #similar to the first function & unittest, check if the function can unflatten a flattened image, test fails if the functions' answer doesn't match my hardcoded answer

        test_actual_output = [0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1] #6x6 flattened image to be checked

        test_expected_output = [
            [0,0,0,0,1,0],
            [1,1,0,0,1,1],
            [0,0,1,1,0,0],
            [1,1,1,1,1,0],
            [1,1,0,1,0,1],
            [0,1,0,0,1,1]
        ] #checking a larger size, 6x6 unflattened image

        self.assertEqual(test_expected_output, unflatten_image (test_actual_output)) #same methodology, see the first assertion comment

        test_actual_output = [1,0,0,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1] #10x10 flattened image to be checked

        test_expected_output = [
            [1,0,0,1,0,1,1,0,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1],
            [0,1,0,1,0,1,0,1,0,1],
            [0,0,0,1,1,1,0,0,0,1],
            [1,1,0,1,0,1,0,1,0,1],
            [0,1,0,0,1,0,0,0,1,0],
            [1,0,0,0,1,1,1,0,1,0],
            [0,1,1,1,1,0,0,0,1,0],
            [0,1,1,0,0,0,0,0,1,1]
        ] #checking for an even larger, 10x10 unflattened image

        self.assertEqual(test_expected_output, unflatten_image (test_actual_output)) #same methodology, see the first assertion comment

    def test_check_adjacent_for_one(self) -> None:
        """
        Verify output of check_adjacent_for_one for three different pixel indexes of an image representing different scenarios.
        """

        test_edge_output = [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1] #unflattened list of all 1's at the edge to be checked and tested

        test_pixel_index = [1,7,13,19,25,31] #here, each test pixel is one position to the right of the '1s' at the edge, it's 'looking' left and checking

        for pixel_index in test_pixel_index: #loop through the chosen test pixels
            self.assertTrue(check_adjacent_for_one(test_edge_output, pixel_index)) #check if function returns True, meaning that the function can successfully determine the value of the pixel at the edge (left of the test pixel indexes)

        test_middle_output = [1,0,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1] #unflattened list with all '1's' in the middle to be checked and tested 

        test_pixel_index = [3,8,13,18,23] #here, each test pixel is one position to the right of the '1's' at the middle, it's 'looking' left and checking 

        for pixel_index in test_pixel_index: #loop through the chosen test pixels
            self.assertTrue(check_adjacent_for_one(test_middle_output, pixel_index)) #check if function returns True (func can determine value of middle pixel successfully)

        test_corner_output = [1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1] #unflattened list with all '1's' at the corners, "look" at the left and right corners and check

        test_pixel_index = [1,2,13,14] #here, each test pixel is in between the '1's' at the corners, it's checking left and right

        for pixel_index in test_pixel_index: #loop through the chosen test pixels
            self.assertTrue(check_adjacent_for_one(test_corner_output, pixel_index)) #check if function returns True (func can successfully determine value of corner pixels)

    def test_pixel_flip(self) -> None:
        """
        Verify output of pixel_flip for a 5x5 image with a budget of 2.
        """
        
        test_unflipped_output = [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1] #this unflipped image will be tested with the function against the hardcoded, actual answer (all possibilities)

        test_budget = 2 #budget set to 2

        test_results = [] #empty list that the function will append the 'test_unflipped_output' into

        test_flipped_possibilities = [
            [0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1], ##the mad lad actually did it and hardcoded 525 values manually - first year programmer type things##
            [0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1], #these are all the possibilities that can be generated from the 'test_unflipped_output' image, this is what the function is checking against
            [0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1]
        ]
        
        pixel_flip(test_unflipped_output, test_unflipped_output, test_budget, test_results) #compare the hardcoded possibilities to the iterated flipped_possibilities that were actually calcualted/created by the code itself from the original list 
        for comparison in test_results: #loop through the test_results (the populated list with the pixel_flip's 'answer' to be checked)
            if comparison not in test_flipped_possibilities: #iterate through the hardcoded all posibilties image
                assert False #if the iterator from the 'test_results' list/answer finds pixels that don't match ('not in') my correct, hardcoded, all possibilities answer, then it is False (test fails, thus the 'pixel_flip' function was coded wrong)

    def test_generate_new_images(self) -> None:
        """
        Verify generate_new_images with image.txt and for each image of the generated images verify that:
        - image is of size 28x28,
        - all values in the generated image are either 1s or 0s,
        - the number of pixels flipped from original image are within budget,
        - all pixels flipped from the original image had an adjacent value of 1.
        """
      ###only unittest not completed due to time constraints###


if __name__ == "__main__":
    unittest.main()
