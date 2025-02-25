import java.util.Optional;

public class SomeSomeSome {

    public static Optional<String> getUserName(int userId) {
        // Simulate fetching user data; user with ID 1 exists, others don't.
        if (userId == 1) {
            return Optional.of("John Doe");
        } else {
            return Optional.empty();
        }
    }

    public static void main(String[] args) {
        Optional<String> userName = getUserName(2); // User ID 2 doesn't exist

        // Check if a value is present before calling get()
        if (userName.isPresent()) {
            String name = userName.get();
            System.out.println("User Name: " + name.toUpperCase());
        } else {
            System.out.println("User not found.");
        }
    }
}
