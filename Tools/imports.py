import re, os, sys, requests, random, time, pytz, uuid, json
from typing import Dict, List, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console

console = Console()

DUMP, LOGIN, FAILED, LOPPING = [], [], [], 0