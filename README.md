readme = r"""
# 🎓 CampusGenAI – Smart Campus Ticket & Information Access Assistant

## 📌 Project Overview

CampusGenAI is a GenAI-powered campus administration assistant designed to securely retrieve and manage information based on a user's Ticket ID and User ID.

The system combines access control, machine learning-based risk prediction, Retrieval-Augmented Generation (RAG), multi-agent processing, and an LLM-based conversational interface.

---

## 🎯 Problem Statement

Design a GenAI-driven administration architecture capable of securely retrieving, managing, and granting information access strictly based on a user's Ticket ID or Transaction ID.

---

## 🎯 Objectives

- Provide secure ticket-based information access.
- Verify users before displaying ticket information.
- Analyze campus-related issues automatically.
- Predict ticket escalation risk.
- Retrieve relevant campus policies using RAG.
- Generate contextual AI responses.
- Prevent unauthorized access to ticket information.

---

## ✨ Key Features

### 🔐 Ticket-Based Access Control

The system verifies:

- Ticket ID
- User ID

Only matching Ticket ID and User ID combinations are authorized.

Example:

CAMP-1001 + STU001 → Access Granted

CAMP-1001 + STU999 → Access Denied

---

### 🤖 AI Ticket Analysis

The system analyzes the ticket issue and identifies:

- Issue Type
- Affected Area

---

### ⚠️ Risk Prediction

A Random Forest machine learning model predicts ticket escalation risk using:

- Priority
- Previous Incidents
- Ticket Age

---

### 📚 Campus Policy RAG

The system retrieves relevant information from the Campus Policies PDF using:

- PDF extraction
- Text chunking
- Sentence Transformers
- FAISS vector search

---

### 🧠 Multi-Agent Architecture

The project contains multiple processing agents:

- Access Control Agent
- Ticket Analyzer Agent
- Risk Prediction Agent
- Policy/RAG Agent
- Response Agent

An orchestrator coordinates the processing flow.

---

### 💬 LLM-Based Response

An OpenRouter-compatible LLM generates a contextual response using authorized ticket information and retrieved campus policy information.

---

## 🏗️ System Architecture

```text
Campus User
     |
     v
Ticket ID + User ID
     |
     v
Access Control
     |
     v
Ticket Database
     |
     v
Multi-Agent AI
     |
     +---- Ticket Analyzer
     |
     +---- Risk Agent
     |
     +---- Policy/RAG Agent
     |
     v
Campus Policy Knowledge
     |
     v
LLM Response Agent
     |
     v
CampusGenAI Response
