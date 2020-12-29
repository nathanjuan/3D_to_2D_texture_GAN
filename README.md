# Universal Texture Extraction with Generative Adversarial Networks
This project utilizes conditional generative adversarial networks to extract a 2D image from a 3D shape. It was developed during the 2019 UCSB Research Mentorship Program under the FourEyes Lab.

The approach that this project takes is to first fill in the background space with the pattern that is on the shape and then fill in the space occupied by the shape with the generated texture. Two GAN's are thus utilized, and the overall process is outlined in the image below.

<p align="center"><img src="https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/ganmethod.png" width="750"></p>

The models were trained with a set of 30,000 images created from 500 images, with varied texture offset and size for each image. For the first GAN, the image inputted into the generative network were images of spheres with applied textures and a black background, and the conditional image that the discriminative network compares with to the output of the generative network is an image with the identical sphere and texture, but with the texture as the background. For the second step, the generative network takes in the output of the first GAN, and the conditional image is a continuous image of the 2D texture without the sphere in the middle. After training, the generative network from GAN #2 gives us the desired output image, a 2D texture image. These models were trained for 10 epochs and were only trained on spherical shapes from the heads-on perspective due to computational cost.

Some example output images of the model are displayed below.

| Input             |  Expected | Generated|
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/input/ex1.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/expected/ex1.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/output/ex1.jpg)
![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/input/ex2.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/expected/ex2.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/output/ex2.jpg)
![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/input/ex3.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/expected/ex3.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/output/ex3.jpg)
![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/input/ex4.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/expected/ex4.jpg) | ![](https://github.com/njuan123/3D_to_2D_texture_GAN/blob/main/sampleimages/output/ex4.jpg)
