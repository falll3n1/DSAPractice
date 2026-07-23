class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # return [[x ^ 1 for x in reversed(img)] for img in image]
        for img in image:
            img.reverse()
            for idx in range(len(img)):
                img[idx] ^= 1 
        return image