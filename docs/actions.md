~~~
# Categories
mutation createCategory {
  createCategory(name: "Fiction") {
    name {
      name
    }
  }
}

query allCategories {
  allCategories {
    id
    name
  }
}

# Movies
query allMovies {
  allMovies {
    id
    name
    year
    category {
      id
      name
    }
  }
}

query detailMovie {
  movie(id: 1) {
    name
  }
}

mutation createMovie {
  createMovie(name: "E.T.", year: 1980, rating: 3, categoryId: 2) {
    name {
      id
      name
      rating
      year
    }
  }
}
~~~