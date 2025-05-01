import os
from bs4 import BeautifulSoup
import numpy as np

# Step 1: Build the link graph
def build_link_graph(folder_path):
    pages = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            with open(os.path.join(folder_path, filename), "r", encoding='utf-8') as file:
                soup = BeautifulSoup(file, "html.parser")
                links = set()
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if href.endswith(".html"):
                        links.add(href)
                pages[filename] = links
    return pages

# Step 2: PageRank algorithm implementation
def compute_pagerank(links, d=0.85, max_iter=100, tol=1e-6):
    pages = list(links.keys())
    N = len(pages)
    page_index = {page: i for i, page in enumerate(pages)}
    M = np.zeros((N, N))

    # Create the transition matrix
    for page in pages:
        if links[page]:
            out_links = links[page]
            for dest in out_links:
                if dest in page_index:
                    M[page_index[dest], page_index[page]] = 1 / len(out_links)
        else:
            # Dangling node: link to all pages equally
            M[:, page_index[page]] = 1.0 / N

    # Initialize PageRank vector
    pr = np.ones(N) / N

    # Iterative computation
    for i in range(max_iter):
        new_pr = (1 - d) / N + d * M @ pr
        if np.linalg.norm(new_pr - pr, 1) < tol:
            print(f"Converged after {i+1} iterations.")
            break
        pr = new_pr

    # Return PageRank scores in dictionary form
    return {pages[i]: pr[i] for i in range(N)}

# Step 3: Main function to run everything
if __name__ == "__main__":
    folder_path = "html_pages"  # Folder with your HTML files
    links = build_link_graph("html_pages")
    print("Link Graph:")
    for page, out_links in links.items():
        print(f"{page} -> {list(out_links)}")

    print("\nCalculating PageRank...")
    pagerank_scores = compute_pagerank(links)

    print("\nPageRank Results:")
    for page, score in sorted(pagerank_scores.items(), key=lambda x: -x[1]):
        print(f"{page}: {score:.4f}")
