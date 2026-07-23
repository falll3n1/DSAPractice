class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()
            for idx in range(len(img)):
                img[idx] ^= 1 

        return image