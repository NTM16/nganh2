import streamlit as st
import pandas as pd
cyclical = pd.read_excel('nckh.xlsx', sheet_name='Consumer Cyclical')
utilities = pd.read_excel('nckh.xlsx', sheet_name='Utilities')
communication = pd.read_excel('nckh.xlsx', sheet_name='Communication Services')
technology = pd.read_excel('nckh.xlsx', sheet_name='Technology')
estate = pd.read_excel('nckh.xlsx', sheet_name='Real Estate')
industrials = pd.read_excel('nckh.xlsx', sheet_name='Industrials')
health = pd.read_excel('nckh.xlsx', sheet_name='Healthcare')
financial = pd.read_excel('nckh.xlsx', sheet_name='Financial Services')
energy = pd.read_excel('nckh.xlsx', sheet_name='Energy')
defensive = pd.read_excel('nckh.xlsx', sheet_name='Consumer Defensive')
materials = pd.read_excel('nckh.xlsx', sheet_name='Basic Materials')
