{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import tweepy\n",
    "import time\n",
    "import json\n",
    "from tweet_config import consumer_key, consumer_secret, access_token, access_token_secret"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Twitter API Keys\n",
    "consumer_key = consumer_key\n",
    "consumer_secret = consumer_secret\n",
    "access_token = access_token\n",
    "access_token_secret = access_token_secret"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Setup Tweepy API Authentication\n",
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Create a function that tweets\n",
    "def TweetOut(tweet_number):\n",
    "    api.update_status(\n",
    "        \"Can't stop. Won't stop. Chatting! This is Tweet #%s!\" %\n",
    "        tweet_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Create a function that calls the TweetOut function every minute\n",
    "counter = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Infinitely loop\n",
    "while(True):\n",
    "\n",
    "    # Call the TweetQuotes function and specify the tweet number\n",
    "    TweetOut(counter)\n",
    "\n",
    "    # Once tweeted, wait 60 seconds before doing anything else\n",
    "    time.sleep(60)\n",
    "\n",
    "    # Add 1 to the counter prior to re-running the loop\n",
    "    counter = counter + 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
