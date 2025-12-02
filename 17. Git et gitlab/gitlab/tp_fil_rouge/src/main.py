from pathlib import Path
import data_loader
import data_cleaner
import data_analyzer


def main():
    try:

        input_file = './data/raw/dirty_cafe_sales.csv'
        output_file = './data/processed/clean_cafe_sales.csv'

        df = data_loader.load_csv(str(input_file))
        print(f"Chargement: {len(df)} lignes")

        df_clean = data_cleaner.clean_data(df)
        print(f"Nettoyage: {len(df_clean)} lignes après nettoyage")

        df_clean.to_csv(output_file, index=False)
        print(f"Données sauvegardées: {output_file}")

        total_revenue = data_analyzer.calculate_total_revenue(df_clean)
        average_ticket = data_analyzer.calculate_average_ticket(df_clean)

        print(f"Chiffre d'affaires: {total_revenue:.2f} euros")
        print(f"Ticket moyen: {average_ticket:.2f} euros")

        return 0

    except Exception as e:
        print(f"Erreur: {str(e)}")
        return 1


if __name__ == '__main__':
    main()