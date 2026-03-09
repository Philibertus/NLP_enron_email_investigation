#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.graph_objects as go
import networkx as nx
from itertools import combinations

def plot_interactive_network(entities_df, min_edge_weight=2, output_file='network_graph.html'):
    """
    Create an interactive network graph from entities dataframe.

    Parameters:
    -----------
    entities_df : pandas.DataFrame
        DataFrame with columns: email_id, type, entity_clean
    min_edge_weight : int, default=2
        Minimum number of co-occurrences to show an edge
    output_file : str, default='network_graph.html'
        Path to save the HTML output file

    Returns:
    --------
    networkx.Graph
        The filtered graph object
    """

    # Build entity graph
    G = nx.Graph()
    for email_id, group in entities_df.groupby("email_id"):
        persons = group[group["type"] == "PERSON"]["entity_clean"].unique()
        for a, b in combinations(persons, 2):
            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)

    # Filter to show only strong connections
    filtered_graph = nx.Graph()
    for u, v, data in G.edges(data=True):
        if data['weight'] >= min_edge_weight:
            filtered_graph.add_edge(u, v, weight=data['weight'])

    # Check if graph is empty
    if len(filtered_graph.nodes()) == 0:
        print(f"No connections found with edge weight >= {min_edge_weight}")
        return filtered_graph

    # Calculate layout
    pos = nx.spring_layout(filtered_graph, k=2, iterations=50, seed=42)

    # Create edge traces
    edge_x = []
    edge_y = []

    for edge in filtered_graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    node_sizes = []
    node_connections = []

    for node in filtered_graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

        # Get connections and weights
        neighbors = list(filtered_graph.neighbors(node))
        num_connections = len(neighbors)
        node_connections.append(num_connections)

        # Create hover text with connection details
        connection_details = []
        for neighbor in neighbors:
            weight = filtered_graph[node][neighbor]['weight']
            connection_details.append(f"  • {neighbor}: {weight} email(s)")

        hover_text = f"<b>{node}</b><br>"
        hover_text += f"Connections: {num_connections}<br>"
        hover_text += "<br>".join(connection_details)

        node_text.append(hover_text)
        node_sizes.append(20 + num_connections * 5)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[node for node in filtered_graph.nodes()],
        textposition="top center",
        textfont=dict(size=10, color='black'),
        hovertext=node_text,
        marker=dict(
            showscale=True,
            colorscale='Viridis',
            size=node_sizes,
            color=node_connections,
            colorbar=dict(
                thickness=15,
                title=dict(
                    text='Number of Connections',
                    side='right'
                ),
                xanchor='left'
            ),
            line=dict(width=2, color='white')))

    # Create figure
    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title=dict(
                        text=f'Interactive Entity Co-occurrence Network (edges ≥ {min_edge_weight})',
                        font=dict(size=16)
                    ),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    plot_bgcolor='white',
                    height=800,
                    width=1000
                    ))

    # Save to HTML
    directory_path = "/Users/leuphi/OneDrive/Philipp/ComputerScience/NLP_enron_email_analysis/data/reports/figures/"
    fig.write_html(directory_path + output_file)

    # Print summary statistics
    print(f"Network Graph Created!")
    print(f"  - Nodes (people): {len(filtered_graph.nodes())}")
    print(f"  - Edges (connections): {len(filtered_graph.edges())}")
    print(f"  - Min edge weight: {min_edge_weight}")
    print(f"  - Saved to: {output_file}")

    return filtered_graph


# Run in terminal:
# jupyter nbconvert --to python plot_interactive_network.ipynb
