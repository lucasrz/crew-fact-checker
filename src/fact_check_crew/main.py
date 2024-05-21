import os
import argparse
from dotenv import load_dotenv
import streamlit as st
from crew import FactCheckCrew
load_dotenv()

# TODO - Implement RAG


def runCrew(api, model):
    return FactCheckCrew(api, model).crew().kickoff()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    runCrew(args.api, args.model)
