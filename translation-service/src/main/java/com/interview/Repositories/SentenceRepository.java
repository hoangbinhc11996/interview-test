package com.interview.Repositories;

import com.interview.DOMs.EnglishVietnameseSentences;
import org.springframework.data.repository.PagingAndSortingRepository;

public interface SentenceRepository extends PagingAndSortingRepository<EnglishVietnameseSentences, Long> {
}

