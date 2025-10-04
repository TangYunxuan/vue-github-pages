let fakeComments = [
  { id: 1, photo_id: 1, author: 'Yunxuan', content: 'So cute!' },
  { id: 2, photo_id: 1, author: 'Gabija', content: 'Meow 🐱' },
]

export const Comment = {
  async list() {
    return fakeComments
  },
  async create(comment) {
    fakeComments.push({
      id: Date.now(),
      ...comment,
    })
  }
}