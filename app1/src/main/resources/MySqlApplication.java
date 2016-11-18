@SpringBootApplication
public class MySqlApplication {
    public static void main(String[] args) {
        SpringApplication.run(MySqlApplication.class, args);
    }

    @Autowired
    DataSource dataSource;

    @PostConstruct
    private void postConstruct() throws Exception {

        try (Connection connection = dataSource.getConnection();
             Statement statement = connection.createStatement()) {

            ResultSet resultSet = statement.executeQuery("SELECT CURRENT_USER();");
            resultSet.next();

            System.out.println("Connection works with User: " + resultSet.getString(1));

            resultSet.close();
        }
    }
}
