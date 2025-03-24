import java.util.*;

class Song {
    private int serialNo;
    private String title;
    private Set<String> artists;
    private int releaseYear;
    private double rating;

    public Song(int serialNo, String title, Set<String> artists, int releaseYear, double rating) {
        this.serialNo = serialNo;
        this.title = title;
        this.artists = artists;
        this.releaseYear = releaseYear;
        this.rating = rating;
    }

    public String getTitle() {
        return title;
    }

    public int getReleaseYear() {
        return releaseYear;
    }

    public Set<String> getArtists() {
        return artists;
    }

    @Override
    public String toString() {
        return "Song{" +
                "serialNo=" + serialNo +
                ", title='" + title + '\'' +
                ", artists=" + artists +
                ", releaseYear=" + releaseYear +
                ", rating=" + rating +
                '}';
    }
}

public class SongCollection {
    private List<Song> songs;

    public SongCollection() {
        songs = new ArrayList<>();
    }

    public void addSong(Song song) {
        songs.add(song);
    }

    public void displaySongs() {
        for (Song song : songs) {
            System.out.println(song);
        }
    }

    public void sortByTitle() {
        songs.sort(Comparator.comparing(Song::getTitle));
    }

    public void sortByReleaseYear() {
        songs.sort(Comparator.comparingInt(Song::getReleaseYear).reversed());
    }

    public List<Song> searchByTitle(String title) {
        List<Song> result = new ArrayList<>();
        for (Song song : songs) {
            if (song.getTitle().equalsIgnoreCase(title)) {
                result.add(song);
            }
        }
        return result;
    }

    public List<Song> songsReleasedThisYear(int currentYear) {
        List<Song> result = new ArrayList<>();
        for (Song song : songs) {
            if (song.getReleaseYear() == currentYear) {
                result.add(song);
            }
        }
        return result;
    }

    public List<Song> songsByArtist(String artist) {
        List<Song> result = new ArrayList<>();
        for (Song song : songs) {
            if (song.getArtists().contains(artist)) {
                result.add(song);
            }
        }
        return result;
    }

    public void displayTitleAndReleaseYear() {
        for (Song song : songs) {
            System.out.println("Title: " + song.getTitle() + ", Release Year: " + song.getReleaseYear());
        }
    }

    public static void main(String[] args) {
        SongCollection collection = new SongCollection();
        collection.addSong(new Song(1, "Song A", new HashSet<>(Arrays.asList("Artist 1", "Artist 2")), 2023, 4.5));
        collection.addSong(new Song(2, "Song B", new HashSet<>(Arrays.asList("Artist 3")), 2022, 4.0));
        collection.addSong(new Song(3, "Song C", new HashSet<>(Arrays.asList("Artist 1")), 2023, 5.0));

        System.out.println("List of Songs:");
        collection.displaySongs();

        System.out.println("\nSorted by Title:");
        collection.sortByTitle();
        collection.displaySongs();

        System.out.println("\nSorted by Release Year (Latest First):");
        collection.sortByReleaseYear();
        collection.displaySongs();

        System.out.println("\nSearch for 'Song A':");
        System.out.println(collection.searchByTitle("Song A"));

        System.out.println("\nSongs Released in 2023:");
        System.out.println(collection.songsReleasedThisYear(2023));

        System.out.println("\nSongs by 'Artist 1':");
        System.out.println(collection.songsByArtist("Artist 1"));

        System.out.println("\nSong Titles and Release Years:");
        collection.displayTitleAndReleaseYear();
    }
}
