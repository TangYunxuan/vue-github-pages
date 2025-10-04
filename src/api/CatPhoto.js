let fakePhotos = [
  {
    id: 1,
    caption: 'First cat photo!',
    image_url: 'https://placekitten.com/400/400',
    likes: 2,
    created_date: '2025-01-01',
  },
  {
    id: 2,
    caption: 'Second cat!',
    image_url: 'https://placekitten.com/401/400',
    likes: 0,
    created_date: '2025-02-01',
  },
]

export const CatPhoto = {
  async list() {
    return fakePhotos.sort((a, b) => new Date(b.created_date) - new Date(a.created_date))
  },
  async update(id, data) {
    fakePhotos = fakePhotos.map((p) => (p.id === id ? { ...p, ...data } : p))
  },
}