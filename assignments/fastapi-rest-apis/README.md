# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework to practice routing, request handling, and JSON response design.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Description
Set up a FastAPI application with a base route and a route that returns a resource by ID.

#### Requirements
Completed program should:

- Define a FastAPI app instance in `starter-code.py`
- Create a root route (`/`) that returns a welcome JSON message
- Create a route `/items/{item_id}` that returns an item by ID
- Return a useful error response when the requested item is not found

### 🛠️ Add Query Parameters and Create Resources

#### Description
Extend the API to support search using query parameters and to add new items through POST requests.

#### Requirements
Completed program should:

- Add a route `/items` that returns all items and supports an optional query parameter for filtering by name
- Define a Pydantic model for item data
- Add a POST route `/items` that accepts JSON body input and returns the created item
- Ensure the API returns valid JSON responses for each endpoint
