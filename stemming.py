{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee355137-2cff-4e44-877a-de943fd4a9f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (3.9.2)\n",
      "Requirement already satisfied: tqdm in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from nltk) (4.67.3)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from nltk) (2026.1.15)\n",
      "Requirement already satisfied: joblib in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from nltk) (1.5.2)\n",
      "Requirement already satisfied: click in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from nltk) (8.3.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\prince yadav\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from click->nltk) (0.4.6)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip available: 22.3.1 -> 26.2.1\n",
      "[notice] To update, run: C:\\Users\\prince yadav\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3625d743-352d-4362-abfe-5b31e57fe49b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt_tab to C:\\Users\\prince\n",
      "[nltk_data]     yadav\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Unzipping tokenizers\\punkt_tab.zip.\n",
      "[nltk_data] Downloading package stopwords to C:\\Users\\prince\n",
      "[nltk_data]     yadav\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Unzipping corpora\\stopwords.zip.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "\n",
    "nltk.download('punkt_tab')\n",
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8046b46e-cdcf-4e6b-8ccd-08528bd6dd93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original: I have three visions for India.\n",
      "Stemmed: three vision india\n",
      "\n",
      "Original: In 3000 years of our history, people from all over \n",
      "               the world have come and invaded us, captured our lands, conquered our minds.\n",
      "Stemmed: year histori peopl world come invad us captur land conquer mind\n",
      "\n",
      "Original: From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,\n",
      "               the French, the Dutch, all of them came and looted us, took over what was ours.\n",
      "Stemmed: alexand onward greek turk mogul portugues british french dutch came loot us took\n",
      "\n",
      "Original: Yet we have not done this to any other nation.\n",
      "Stemmed: yet done nation\n",
      "\n",
      "Original: We have not conquered anyone.\n",
      "Stemmed: conquer anyon\n",
      "\n",
      "Original: We have not grabbed their land, their culture, \n",
      "               their history and tried to enforce our way of life on them.\n",
      "Stemmed: grab land cultur histori tri enforc way life\n",
      "\n",
      "Original: Why?\n",
      "Stemmed: \n",
      "\n",
      "Original: Because we respect the freedom of others.That is why my \n",
      "               first vision is that of freedom.\n",
      "Stemmed: respect freedom first vision freedom\n",
      "\n",
      "Original: I believe that India got its first vision of \n",
      "               this in 1857, when we started the War of Independence.\n",
      "Stemmed: believ india got first vision start war independ\n",
      "\n",
      "Original: It is this freedom that\n",
      "               we must protect and nurture and build on.\n",
      "Stemmed: freedom must protect nurtur build\n",
      "\n",
      "Original: If we are not free, no one will respect us.\n",
      "Stemmed: free one respect us\n",
      "\n",
      "Original: My second vision for India’s development.\n",
      "Stemmed: second vision india develop\n",
      "\n",
      "Original: For fifty years we have been a developing nation.\n",
      "Stemmed: fifti year develop nation\n",
      "\n",
      "Original: It is time we see ourselves as a developed nation.\n",
      "Stemmed: time see develop nation\n",
      "\n",
      "Original: We are among the top 5 nations of the world\n",
      "               in terms of GDP.\n",
      "Stemmed: among top nation world term gdp\n",
      "\n",
      "Original: We have a 10 percent growth rate in most areas.\n",
      "Stemmed: percent growth rate area\n",
      "\n",
      "Original: Our poverty levels are falling.\n",
      "Stemmed: poverti level fall\n",
      "\n",
      "Original: Our achievements are being globally recognised today.\n",
      "Stemmed: achiev global recognis today\n",
      "\n",
      "Original: Yet we lack the self-confidence to\n",
      "               see ourselves as a developed nation, self-reliant and self-assured.\n",
      "Stemmed: yet lack see develop nation\n",
      "\n",
      "Original: Isn’t this incorrect?\n",
      "Stemmed: incorrect\n",
      "\n",
      "Original: I have a third vision.\n",
      "Stemmed: third vision\n",
      "\n",
      "Original: India must stand up to the world.\n",
      "Stemmed: india must stand world\n",
      "\n",
      "Original: Because I believe that unless India \n",
      "               stands up to the world, no one will respect us.\n",
      "Stemmed: believ unless india stand world one respect us\n",
      "\n",
      "Original: Only strength respects strength.\n",
      "Stemmed: strength respect strength\n",
      "\n",
      "Original: We must be \n",
      "               strong not only as a military power but also as an economic power.\n",
      "Stemmed: must strong militari power also econom power\n",
      "\n",
      "Original: Both must go hand-in-hand.\n",
      "Stemmed: must go\n",
      "\n",
      "Original: My good fortune was to have worked with three great minds.\n",
      "Stemmed: good fortun work three great mind\n",
      "\n",
      "Original: Dr. Vikram Sarabhai of the Dept.\n",
      "Stemmed: vikram sarabhai dept\n",
      "\n",
      "Original: of \n",
      "               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.\n",
      "Stemmed: space professor satish dhawan succeed brahm prakash father nuclear materi\n",
      "\n",
      "Original: I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.\n",
      "Stemmed: lucki work three close consid great opportun life\n",
      "\n",
      "Original: I see four milestones in my career\n",
      "Stemmed: see four mileston career\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from nltk.stem import PorterStemmer\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "paragraph = \"\"\"I have three visions for India. In 3000 years of our history, people from all over \n",
    "               the world have come and invaded us, captured our lands, conquered our minds. \n",
    "               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,\n",
    "               the French, the Dutch, all of them came and looted us, took over what was ours. \n",
    "               Yet we have not done this to any other nation. We have not conquered anyone. \n",
    "               We have not grabbed their land, their culture, \n",
    "               their history and tried to enforce our way of life on them. \n",
    "               Why? Because we respect the freedom of others.That is why my \n",
    "               first vision is that of freedom. I believe that India got its first vision of \n",
    "               this in 1857, when we started the War of Independence. It is this freedom that\n",
    "               we must protect and nurture and build on. If we are not free, no one will respect us.\n",
    "               My second vision for India’s development. For fifty years we have been a developing nation.\n",
    "               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world\n",
    "               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.\n",
    "               Our achievements are being globally recognised today. Yet we lack the self-confidence to\n",
    "               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?\n",
    "               I have a third vision. India must stand up to the world. Because I believe that unless India \n",
    "               stands up to the world, no one will respect us. Only strength respects strength. We must be \n",
    "               strong not only as a military power but also as an economic power. Both must go hand-in-hand. \n",
    "               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of \n",
    "               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.\n",
    "               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. \n",
    "               I see four milestones in my career\"\"\"\n",
    "\n",
    "sentences = nltk.sent_tokenize(paragraph)\n",
    "\n",
    "stemmer = PorterStemmer()\n",
    "stop_words = set(stopwords.words('english'))\n",
    "\n",
    "for sentence in sentences:\n",
    "    words = nltk.word_tokenize(sentence)\n",
    "\n",
    "    stemmed_words = [\n",
    "        stemmer.stem(word)\n",
    "        for word in words\n",
    "        if word.lower() not in stop_words and word.isalpha()\n",
    "    ]\n",
    "\n",
    "    print(\"Original:\", sentence)\n",
    "    print(\"Stemmed:\", \" \".join(stemmed_words))\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6645e45e-379b-4a4c-92bd-23f678ba6361",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "mykernel",
   "language": "python",
   "name": "mykernel"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
