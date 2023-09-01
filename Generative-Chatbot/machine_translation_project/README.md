# Set Up The Code
Clone the Repo to your local machine. You should have following files:
deu.txt
preprocessing.py
training_model.py
test_function.py

You can download a different language-pair file from [here](http://www.manythings.org/anki/)
You can move the [your-language].txt file into the same directory (folder) as the machine translation code to make it slightly easier to set up.

# Preprocessing
1. Open preprocessing.py in a code editor or IDE.
2. Change data_path to the file path of [your-language].txt. If it’s in the same directory as preprocessing.py, then all you need is the file name.
3. In preprocessing.py, adjust the number of lines of training data you want to work with. We’re giving you a default of 500, but depending on how much you want to tax your computer, you can go up to 123,000 lines. Whatever you choose, this should be a much higher number than 500. I used 10000 but that took a minute to process.
4. Run the code and make sure everything works, error-free. Remember that more training data leads to better results for machine translation.
5. At the end of preprocessing.py, print out list(input_features_dict.keys())[:50], reverse_target_features_dict[50], and the length of input_tokens. Does each look how you expected?

# The Training Model
1. Open training_model.py. This is where the training model is built and trained.
2. Change the values for the following:
latent_dim: Choose a latent dimensionality for your model. Keras’s documentation uses 256, but you can adjust as you see fit.

batch_size: You can choose to adjust this or not at this point. This determines how many sentences are used at a time for training.

epochs: This should be a larger number (Keras’s documentation uses 100) so that the seq2seq model has many chances to improve. Bear in mind that a larger number of epochs will also take your computer a lot longer to process. If you don’t have the ability to leave your computer running for several hours for this project, then choose a number that is less than 100.

Run the code to generate your model. In the terminal, you should see a summary of the model printed out. Meanwhile, you’ll also see a new file in the directory called training_model.h5. This is where your seq2seq training model is saved so that it’s quicker for you to run your code during testing.
Note that you may get the following error when attempting to run your program on a regular computer that uses CPU processing:

OMP: Error #15: Initializing libiomp5.dylib, but found libiomp5.dylib already initialized.
OMP: Hint: This means that multiple copies of the OpenMP runtime have been linked into the program. That is dangerous, since it can degrade performance or cause incorrect results. The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, e.g. by avoiding static linking of the OpenMP runtime in any library. As an unsafe, unsupported, undocumented workaround you can set the environment variable KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, but that may cause crashes or silently produce incorrect results. For more information, please see http://www.intel.com/software/products/support/.
Abort trap: 6

Below the import statements on training.py, there’s are a couple lines commented out, which you can uncomment to make the program run. However, if you are concerned about your computer crashing, you may want to hold off completing this project until you have access to a faster computer with GPU processing.

# The Test Model and Function
1. Open test_function.py. You’ll see that we’ve imported several variables from the preprocessing and training steps of the program.
2. In the for loop at the bottom of the file, increase the range if you want to see more sentences translated — this is up to you. Of course, more sentences will increase the amount of time your computer will require for the translation.
3. When you feel ready for your computer to spend awhile training and translating, run the code. This is going to take awhile — from 20 minutes to several hours, so make sure your computer is plugged in. You should see each epoch appear in the terminal as a fraction of the total number of epochs you selected. For example, 16/100 indicates the program has reached the 16th epoch out of 100 total epochs. You’ll also see the loss go down for each epoch, which is very exciting — this is the model getting more accurate!
4. When your computer finishes the full process, you’ll see the translations appear. You can use a speaker of that language or Google Translate to see how accurate they are.